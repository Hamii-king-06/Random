import os,re,sys,platform
os.system('git pull')
os.system('pkg install play-audio')
import requests
print("join My Facebook Group")
os.system("xdg-open https://facebook.com/groups/492909121746564/")
print("FOLLOW MY PAGE THIS IS IMPORTANT")
os.system("xdg-open https://www.facebook.com/hamiicammands")



bit = platform.architecture()[0]
if bit == '64bit':
    from Xyz import XYZ
    XYZ()
elif bit == '32bit':
    from Xyz32 import XYZ
    XYZ()
