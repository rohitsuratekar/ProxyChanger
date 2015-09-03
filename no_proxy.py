#One click Proxy changer
#Tested on Windows 7, 8, 8.1 and 10
#You need administrator access to execute this code
#This script will change Firefox proxy settings to No proxy from "proxy.old.domain" and port to "3128"

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

set_key('ProxyEnable', 0)
set_key('ProxyOverride', u'*.local;<local>')  # Bypass the proxy for localhost
set_key('ProxyServer', u'proxy.old.domain:3128')

#For Mozilla Firefox
first_string= os.getenv('APPDATA')
file_change = first_string+'\Mozilla\Firefox\Profiles'
os.chdir(file_change)
for file in glob.glob('*.default'):
    pro_name = '\\'+file
file_final = file_change+pro_name+'\\prefs.js'
text_sreach = 'user_pref("network.proxy.type", 1);'
text_replace = 'user_pref("network.proxy.type", 0);'
filedata = None
with open(file_final, 'r') as file :
  filedata = file.read()
filedata = filedata.replace(text_sreach, text_replace)
with open(file_final, 'w') as file:
  file.write(filedata)
