import os, platform
os.system("pkg install play-audio")
os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':
    os.system("play-audio WELCOME_TO_HAMII_RANDOM_CLONE_TOOL.mp3") 
    from FUCK64 import xyz
    xyz()


elif bit == '32bit':

    from FUCK32 import xyz
    os.system("play-audio WELCOME_TO_HAMII_RANDOM_CLONE_TOOL.mp3") 
    xyz()

