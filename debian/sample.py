import os
import subprocess

print('Hello This run from docker')
output = subprocess.getoutput('apt show postgresql')
# apt list --installed

print(output)
