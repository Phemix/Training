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

The following directories fall under the local domain:
• /Applications
• /Developer
• /Library
