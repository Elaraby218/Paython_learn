# check if the file exist or not

import os
path = "C:\\Users\\Administrator\\Desktop\\Meetint.txt.bak"

if os.path.exists(path):
    print("That location exists ")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("that location doesnt exist")