import os
path = input("path>>")
os.symlink(path, path + '-link')