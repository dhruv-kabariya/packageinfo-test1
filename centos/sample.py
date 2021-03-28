import os
import subprocess

print('Hello This run from docker')
output = subprocess.getoutput('yum info postgresql')
print(output)
