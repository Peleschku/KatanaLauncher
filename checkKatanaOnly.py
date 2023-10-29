import os
from os.path import isfile, join


checkDirectory = os.listdir('C:\Program Files\Foundry')
prefix = 'Katana'

katanaInstalls = []


for k in checkDirectory:
    if k.startswith(prefix):
        katanaInstalls.append(k)
    else:
        continue
print(katanaInstalls)



