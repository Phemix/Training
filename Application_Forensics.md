                                            APPLICATIONS
                                            
                                            
 Default application installation directory
 --------------------------------------
 Most commonly, this is C:\Program Files. On 64-bit systems, be sure to check C:\Program Files (x86), the location where 32-bit applications are installed by default.
 
 
 Default application data directories
 ------------------------------
  In Windows Vista and newer versions, check all directories one level under C:\ProgramData and C:\Users\{username}\AppData.4
  
  Registry uninstall information 
  -----------------
  * Examine the registry keys under HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall. 
  * On 64-bit versions of Windows, be sure to check HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall, which holds information on any 32-bit applications installed
  
  Default registry configuration data locations 
  ---------------
   * Check all sub-keys one level down from HKLM\SOFTWARE.
   * On 64-bit systems, be sure to check HKLM\SOFTWARE\Wow6432Node
   
   Default application installation directory (OS X)
   -------------
   * The default installation directory for applications in OS X is /Applications.
   * OS X applications generally place user-specific data within directories under the user’s profile. The default location is /Users/{profile}/Library/Application Support.
   
   Application artifacts for Linux distros
   --------------------------
   • Systemwide configuration data  In most Linux distributions, the /etc and /usr/local/etc/directories are the primary locations where systemwide application configuration data is stored.
• User application data  User-specific application data is typically found in subdirectories under the user’s home directory, by default /home/{username}.
• Executable locations  The standard directories where you will find executables are /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, and /usr/local/sbin.
• Add-on software  A location where some third-party applications and application data are installed to is /opt.


Package Managers
----------------
Sometimes a faster way to get the answers you are looking for is to simply query the package manager

* RPM-based distributions  The RPM Package Manager (RPM) is used by a number of popular Linux distributions. 
*** inset RPM queries ***
• Debian-based distributions  Debian-based distributions use the dpkg package manager, and by default its packages are named with a .deb extension.
   dpkg --get-selections

Internet Explorer
-------------------
Artifact            Location
Autocomplete <br /> 
                    HKEY_CURRENT_USER\​Software\Microsoft\​Internet Explorer\​IntelliForms\Storage1<br /> 
                    HKEY_CURRENT_USER\​Software\Microsoft\​Internet Explorer​\IntelliForms​\Storage2
Typed URLs<br /> 
                    HKEY_CURRENT_USER\Software​\Microsoft\Internet Explorer\TypedURLs<br /> 
                    HKEY_CURRENT_USER\​Software\Microsoft\​Internet Explorer\​TypedURLsTime<br /> 
Preferences<br /> 
                    HKEY_CURRENT_USER\​Software\Microsoft\​Internet Explorer<br /> 
Cache<br /> 
                    C:\Users\{username}\AppData\Local​\Microsoft\Windows​\Temporary Internet Files\<br /> 
Bookmarks<br /> 
                    C:\Users\{username}​\Favorites<br /> 
Cookies<br /> 
                    C:\Users\{username}\AppData\​Roaming\Microsoft\​Windows\Cookies<br /> 
                    C:\Users\{username}​\AppData\Roaming\​Microsoft\Windows\Cookies\Low<br /> 
ESE  The ESE (Extensible Storage Engine) database replaced the index.dat file functionality beginning with IE version 10. Internet browsing history is stored in a single database file per user. Microsoft has used ESE in the past for LDAP, Exchange, and the Windows Search Index. There are tools on the market that can read and interpret this data, which we cover shortly. The following table lists the location and file names for IE ESE databases:

Windows 7 – 8.1<br /> 
                     {systemdrive}\Users\{username}\AppData\Local\Microsoft\Windows\WebCache<br /> 
                    • WebCacheV01.dat<br /> 
                    • WebCacheV16.dat<br /> 
                    • WebCacheV24.dat<br /> 
                    
Google Chrome
--------------------
Windows Vista/7/8<br /> 
                      C:\Users\{username}​\AppData\Local\​Google\Chrome\<br /> 
Linux<br /> 
                      /home/{username}/.config/google-chrome/<br /> 
OS X<br /> 
                      /Users/{username}/​Library/Application Support/Google/Chrome/
   
      History
      -------------
      the History file is just a SQLite database
      The file Archived History is a stripped-down version of History that tracks activity older than three months. It drops a few of         the ancillary tables Chrome uses and keeps the core “urls” and “visits” tables,
   
      Cache
      --------------
      Chrome’s cache is located at User Data\Default\Cache
  
  
 
 
