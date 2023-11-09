import os
from os.path import isfile, join
import subprocess

'''
Making sure that only Katana installs are being detected in the
intstalls directory, and not any other installs fninstall may have made.

checkDirectory = os.listdir('C:\Program Files\Foundry')
prefix = 'Katana'

katanaInstalls = []


for k in checkDirectory:
    if k.startswith(prefix):
        katanaInstalls.append(k)
    else:
        continue
print(katanaInstalls)


katanaInstall = 'Katana6.0v2'

for launch in katanaInstall:
    launchDir = os.path.join('C:\Program Files', katanaInstall, "bin")
    insideBin = os.listdir(launchDir)
    
    if os.path.isfile('katanaBin.exe'):
        subprocess.run()
    else:
        continue

'''

katanaInstall = 'Katana6.0v2'
delightPath = os.path.join('C:\\Program Files\\Foundry', katanaInstall, '3Delight')
print(delightPath)

myEnvironment["DEFAULT_RENDERER"] = 'dl'
myEnvironment["DELIGHT"] = 'C:/Program Files/3Delight'
myEnvironment["PATH"] += f';{myEnvironment["DELIGHT"]}/bin'
myEnvironment["KATANA_RESOURCES"] += f';{myEnvironment["DELIGHT"]}/3DelightForKatana'
