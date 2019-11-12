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
      
      Cookies
      -----------
      The file Cookies contains all cookies the browser saves; Chrome uses a database rather than many individual text files. 
      
      Downloads
      --------------
       The History file also contains details about files that a user saves using Chrome. Old versions of Chrome have all this data in          the “downloads” table

Mozilla FireFox
------------------

        Data Formats and Locations
        ---------------------------
        Mozilla and Chrome have a number of similarities in the way they store data. Mozilla, like Chrome, stores nearly all of its data         in files, and Mozilla uses SQLite and JSON formats for most of its data storage.
        
        Windows Vista and newer
        C:\Users\{username}​\AppData\Roaming\​Mozilla\Firefox
        C:\Users\{username}\AppData\Local\Mozilla\Firefox (Cache)
        Linux
        /home/{username}/.mozilla/firefox /home/{username}/.​cache/.mozilla/firefox (Cache)
        OS X
        /Users/{username}​/Library/Application Support/Firefox /Users/{username}/Library​/Caches/Firefox (Cache)
        
E-MAIL CLIENTS
------------------

 The body is the actual content of the e-mail, such as text or attachments. It is common for the body to be encoded in the Multipurpose Internet Mail Extensions (MIME) format. This encoding standard was created so newer multimedia contents are handled correctly as the e-mail passes through different types e-mail systems.
        
        Data Storage Locations
        ---------------------
        C:\Users\{Windows_profile}​\AppData\Local\Microsoft​\Outlook\{login_name}.ost
        C:\Users\{Windows_profile}​\Documents\Outlook Files\Outlook.pst
        
A reliable place to check for data files that are configured in Outlook is the Windows registry key HKEY_CURRENT_USER\Software\Microsoft\Office\{version}\Outlook\Search\Catalog, where {version} is the “short” Office version number.


        Data Format
        -------------
        Outlook uses a file format called the Personal Folder File (PFF). In a Microsoft Exchange–based environment, Outlook will store         a copy of e-mail offline in a file called the Offline Storage Table (OST), which is a form of PFF. In non-Exchange environments,         such as Post Office Protocol (POP), or in Outlook archives, the file format used is the Personal Storage Table (PST), also a             form of PFF.
  
  Microsoft Outlook for Mac
  ---------------------------
  
Outlook’s features are also similar to Apple Mail; however, Outlook for Mac allows users to set up Exchange server-side rules and integrate with other Exchange and Microsoft enterprise features, such as Lync. 


          Data Storage Location and Format
          --------------------------
          Microsoft Outlook for Mac 2011 stores user data under the directory /Users/{profile}/Documents/Microsoft User Data/Office 2011           Identities.
          
          
          Tools
          ----------------
          A tool that specifically supports Outlook for Mac 2011, such as Aid4Mail or Emailchemy, is recommended. Not all tools support           properly handling Unicode, and even though it may just be standard ASCII characters in Unicode format, they may not handle               them properly.
  
  
 
 
