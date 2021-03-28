import os
import subprocess

print('Hello This run from docker')
output = subprocess.getoutput('packman -Ss postgresql')
# apt list --installed

print(output)
