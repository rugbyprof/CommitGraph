import subprocess

subprocess.call(['python3','genFakeFile.py'])
subprocess.call(['git','add','.'])
subprocess.call(['git','commit','-m','adding fake files ... again'])
subprocess.call(['git','push','origin','master'])