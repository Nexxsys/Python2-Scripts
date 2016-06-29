import os
myCWD = os.getcwd()
dirContents = os.listdir(myCWD)
for names in dirContents:
    print names
