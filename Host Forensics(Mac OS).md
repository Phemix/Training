                                          MAC FORENSIC ANALYSIS
                            
                            
                            
HFS+ AND FILE SYSTEM ANALYSIS
------------------------------------

Notably absent from the list is native file system support for sparse files. These are common on most moderns file systems and allow a system to efficiently store files that contain empty space.

Volume Layout
------------------------
An HFS+ volume consists of nine structures: boot blocks, a volume header, the allocation file, the extents overflow file, the catalog file, the attributes file, the startup file, the alternate volume header, and reserved blocks. 

Boot Blocks
----------------------
The first 1,024 bytes of the volume are reserved for use as boot blocks and may contain information required at startup.

Volume Header and Alternate Volume Header
------------------------
The volume header is always located 1,024 bytes (two 512-byte allocation blocks) from the beginning the volume. The volume header contains information about the volume, including the location of the other structures.

HFS+ dates are stored in seconds since midnight January 1, 1904 GMT. An important thing to note is the volume creation date stored in the volume header is local time, not GMT. An HFS+ volume may have four dates: create date, modify date, backup date, and checked date.

The alternate volume header is always located 1,024 bytes from the end of the volume and occupies 512 bytes. The alternate volume header is a copy of the volume header that allows for recovery in the event the volume header becomes corrupted.

On the topic of date stamps, HFS+ stores four dates for each file. It stores the normal file access, file modify, and inode change times

Allocation File
----------------
The allocation file is just what it sounds like—a record of available allocation blocks. It contains a bit for every block; when a bit is not set, it indicates the space is available for use.

Extents Overflow File
---------------------------
The catalog B-tree maintains a record of the first eight extents. If there are more than eight extents in a fork, the remaining ones are stored in the extents overflow file.

Catalog File
-----------------
The catalog file is a file detailing the hierarchy of files and folders in the volume. Each file and folder in the volume has a unique catalog node ID (CNID). 

Attributes File
----------------
The attributes file is an optional part of the file system standard. It is defined for use by named forks

Extended information stored for a file may be examined with the xattr command.

Startup File
-------------------
The startup file is intended to hold information needed when booting a system that does not have built-in (ROM) support for HFS+. Mac OS X does not use the startup file

Managed Storage
-------------
The daemon that manages this function is called revisiond, and it maintains data on volumes under the “hidden” directory /.DocumentRevisions-V100. Under that directory, the service stores the file data in PerUID and the database in db-V1. To review the files stored in the versioning system, open the SQLite database/.DocumentRevisions-V100/db-V1/db.sqlite. 

File System Layout
---------------------
Apple defines four “domains” for data classification. The four domains are local, system, network, and user. Each domain is defined by a set of paths, resources, and access controls. 

The local domain consists of applications and configurations that are shared among all users of the system. A user requires administrative privileges to modify the data in this domain

The following directories fall under the local domain:
• /Applications
• /Developer
• /Library

The second domain, system, contains data installed by Apple as well as a few specialized low-level utilities. Files in the following directories require administrative privileges to modify. Included in the system domain are all of the traditional Unix structures: /bin, /usr, /dev, /etc

The third domain, network, is where applications and data is stored that will be shared among a network of systems and users. In practice, this domain is rarely populated with data. This is located under the /Network directory.

The fourth domain, user, is the source of data that will apply to most other investigations. The user domain contains user home directories and a shared directory. Generally, all user-created content and configurations will be found under the /Users top-level directory.

Local domain BreakDown
-------------------------

Application Bundles are directory structures in a standardized format and extension. They contain nearly everything an application requires in order to run,

The most common Application Bundle extensions are
• .app  Launchable applications
• .framework  Dynamic shared libraries and their resources
• .plugin  Helper applications or drivers for other applications
• .kext  Dynamically loadable kernel modules


/Library/Application Support | /User/username/​Library/Application Support                        
This directory is used by applications to store settings, caches, license                                                        information, and nearly anything else desired by the developer.

/Library/Caches | /System/Library/​Caches | /User/username​/Library/Caches
This directory is used by applications to store temporary data. The Caches directory holds a significant amount of potentially relevant data. We cover a few applications that make use of this directory in Chapter 14.

/Library/Logs | /User/username​/Library/Logs
This directory contains various application logs. This directory is one of the most important to review in this domain

/Library/Preferences | /User/username​/Library/Preferences
This directory stores application preferences, if the application allows a system API to manage them. Generally, the data files are in a property list (plist) format, which makes examination fairly simple. This directory can be (very) loosely compared to the Software hive from a Windows system.

/Library/Receipts/ |User/username​/Library/Receipts
When applications are added to the system, the files in /Library/Receipts are updated. A plist named InstallHistory.plist contains information about every application installed via the OS’s installer or update framework.

/Library/WebServerApache, 
installed on every copy of Mac OS X, is started when a user turns on Web Sharing. Apache’s Document Root directory is this folder in /Library.


System Domain Drilldown
-----------------

In the /System directory, you’ll find a structure that resembles the /Library directory discussed earlier. Here, you will find many locations where applications can maintain persistence on a Mac OS X system.


The User Domain
---------------------------
The user domain is where most, if not all, user-created content resides. In the directory /Users, you’ll find a directory for each individual account, as well as a shared directory.


When a new user account is created, the user’s home directory is populated with the directories listed below:
Applications, Desktop, Document, Libraries, Movies, Public

Directory Services does not store user account information within traditional Unix files such as /etc/passwd and /etc/groups. Instead, the data for the local system is located in SQLite databases and binary-formatted property lists.

The Evidence
The Directory Service stores its data in /private/var/db/dslocal. Within this directory, the databases (or nodes) for the local system reside within nodes/Default. As you examine the files, you will notice directories and plist files that correspond to many Unix environment configuration options. In addition to user accounts and groups, you’ll find that Directory Services manages several other configuration items:
• aliases  Local routing for internal mail
• computers  Kerberos information for the local system
• config  Kerberos and Share information
• network  Loopback network information
• sharepoints  Directories that are shared out to other systems through SMB or AFP

A periodic CRON job backs up this entire directory. The backup file is located at /private/var/db/dslocal-backup.xar and is a normal gzip tar file.


User Accounts  
------------
In the “users” node, a binary plist file represents each user account. The plist file typically includes properties:

Sharepoints  
-----------
The sharepoints node contains a binary plist for each shared directory. When a user turns on File Sharing for a directory, the system creates a binary plist that contains 13 attributes, including the status of the share for AFP, SMB, and FTP, the sharepoint names for each service, and the shared path. 

Trash and Deleted Files
----------------------
Like Linux and Windows, files deleted via the graphical user interface are retained temporarily before permanent deletion. Mac OS X stores files marked for deletion in three different locations, depending on the location of the original file and the user that performs the deletion:
• /.Trashes  Volume-wide trash folder
• ~/.Trash  User-specific trash folder
• /private/var/root/.Trash  Root user’s trash folder

System Auditing and Databases
Mac OS X has a powerful auditing system known as the Open Source Basic Security Module (OpenBSM). The logs are located in /private/var/audit. The configuration files for OpenBSM are in /etc/security

The primary file, audit_control, specifies that the log data is stored in /private/var/audit. 

You can improve the fidelity of the data logged by auditd before an incident occurs. In the auditd configuration file, /etc/security/audit_control, make the following changes and reboot:

flags:all
naflags:lo

System and Application Logging
--------------------------------------
On Mac OS X workstations, you’ll find logs and a great number of forensic artifacts in the three primary locations listed next (note that /var/log is a symlink to /private/var/log on the file system):
• /private/var/log
• /Library/Logs
• /Users/username/Library/Logs
• /Users/username

When log files are stored in a binary format, such as through Apple System Log (ASL) or auditd, you need to use a set of utilities to convert them to a human-readable form. 

The syslog and the Apple System Log (ASL) daemons are the processes responsible for most log data on Mac OS X. The largest volume of log data can be found in /private/var/log, so we will start there.

The ASL configuration file contains some entries that are traditionally defined in /etc/syslog.conf.

ASL will store data in the directory /private/var/log/asl.

OpenBSM process audit log data is stored in /private/var/audit. This logging facility tracks all authentication events and stores them in a non-ASCII file format.

The extracts shown were generated with the command line praudit –s [filename]. We manually searched for the authentication events.

/private/var/log/system.log shows system logs

We mentioned earlier that airportd maintained a list of recent 802.11 station associations in /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist




