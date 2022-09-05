import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from arch64 import xyz

    xyz()

elif bit == '32bit':

    from arch32 import xyz

    xyz()



