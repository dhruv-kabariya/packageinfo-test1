import os
import subprocess

print('Hello This run from docker')
output = subprocess.getoutput('zypper info postgresql')
print(output)
