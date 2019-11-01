On Windows, you can create a batch file to run this program with the WIN-R Run window. (For more about batch files, see Appendix B.) Type the following into the file editor and save the file as pw.bat in the C:\Windows folder:


@py.exe C:\Python34\pw.py %*
@pause


With this batch file created, running the password-safe program on Windows is just a matter of pressing WIN-R and typing pw <account name>.
