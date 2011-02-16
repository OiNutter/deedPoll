#!c:\Python31\python.exe
#Filename: deedPoll.py

import os
import sys

for arg in sys.argv:
	print(arg)

target = sys.argv[1]
name = sys.argv[2]

os.rename(target,name);

