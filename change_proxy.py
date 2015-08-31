#One click Proxy changer
#Tested on Windows 7, 8, 8.1 and 10
#You need administrator access to execute this code
#This script will change Firefox proxy settings to "proxy.yourdomain.com" from "proxy.old.domain" and port to "3128"
import os
import sys
import glob
import win32com.shell.shell as shell
import _winreg as winreg

#For internet explorer
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

set_key('ProxyEnable', 1)
set_key('ProxyOverride', u'*.local;<local>')  # Bypass the proxy for localhost
set_key('ProxyServer', u'proxy.yourdomain.com:3128')

#For Mozilla Firefox
first_string= os.getenv('APPDATA')  #Get username on Windows
file_change = first_string+'\Mozilla\Firefox\Profiles'
os.chdir(file_change)
for file in glob.glob('*.default'):    #Check firefox profile name folder
    pro_name = '\\'+file
file_final = file_change+pro_name+'\\prefs.js'   #Preference file
text_sreach = 'user_pref("network.proxy.http", "proxy.old.domain");'
text_replace = 'user_pref("network.proxy.http", "proxy.yourdomain.com");'
text_sreach2 = 'user_pref("network.proxy.backup.ftp", "proxy.old.domain");'
text_replace2 = 'user_pref("network.proxy.backup.ftp", "proxy.yourdomain.com");'
text_sreach3 = 'user_pref("network.proxy.backup.socks", "proxy.old.domain");'
text_replace3 = 'user_pref("network.proxy.backup.socks", "proxy.yourdomain.com");'
text_sreach4 = 'user_pref("network.proxy.ftp", "proxy.old.domain");'
text_replace4 = 'user_pref("network.proxy.ftp", "proxy.yourdomain.com");'
text_sreach5 = 'user_pref("network.proxy.socks", "proxy.old.domain");'
text_replace5 = 'user_pref("network.proxy.socks", "proxy.yourdomain.com");'
text_sreach6 = 'user_pref("network.proxy.ssl", "proxy.old.domain");'
text_replace6 = 'user_pref("network.proxy.ssl", "proxy.yourdomain.com");'
text_sreach7 = 'user_pref("network.proxy.backup.ssl", "proxy.old.domain");'
text_replace7 = 'user_pref("network.proxy.backup.ssl", "proxy.yourdomain.com");'
text_sreach8 = 'user_pref("network.proxy.type", 0);'
text_replace8 = 'user_pref("network.proxy.type", 1);'
filedata = None
with open(file_final , 'r') as file :
  filedata = file.read()
filedata = filedata.replace(text_sreach, text_replace)
filedata = filedata.replace(text_sreach2, text_replace2)
filedata = filedata.replace(text_sreach3, text_replace3)
filedata = filedata.replace(text_sreach4, text_replace4)
filedata = filedata.replace(text_sreach5, text_replace5)
filedata = filedata.replace(text_sreach6, text_replace6)
filedata = filedata.replace(text_sreach7, text_replace7)
filedata = filedata.replace(text_sreach8, text_replace8)
with open(file_final, 'w') as file:
  file.write(filedata)
