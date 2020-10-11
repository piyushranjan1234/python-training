import os
import fnmatch

for root, dirs, files in os.walk("."):
    for filename in files:
        if fnmatch.fnmatch(filename,"*.py"):
            print(filename)
        
