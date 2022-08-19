import os, platform
os.system("pkg install play-audio")
os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from FUCKING_HARD64 import xyz

    xyz()

elif bit == '32bit':

    from FUCKING_HARD import xyz

    xyz()

