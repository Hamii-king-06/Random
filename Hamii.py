Qimport os,re,sys,platform
os.system('git pull')

import requests
print("FOLLOW MY PAGE THIS IS IMPORTANT")
os.system("xdg-open https://www.facebook.com/hamiicammands")



bit = platform.architecture()[0]
if bit == '64bit':
    from Xyz import XYZ
    XYZ()
elif bit == '32bit':
    from Xyz32 import XYZ
    XYZ()
