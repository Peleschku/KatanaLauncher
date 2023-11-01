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

subprocess.call(['C:\\Program Files\\Katana6.0v2\\bin\\katanaBin.exe'])

