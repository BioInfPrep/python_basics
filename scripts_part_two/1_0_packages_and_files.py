# importing packages

# option 1 - import whole package
from os import listdir as ld
from os import listdir
import os
print(os.listdir())

# option 2 - only a few functions
print(listdir())

# option 3 - rename function or packages
print(ld())

# printing lengths of listdir
# remember the linux ways for travesing the file sys.!
print(len(ld()))
print(len(ld(".")))
print(len(ld("..")))
print(len(ld("Desktop")))
