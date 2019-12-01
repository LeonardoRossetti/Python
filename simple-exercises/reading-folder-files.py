import glob
import os

os.chdir("C:/Users/E6530/Pictures/Canon")
for file in glob.glob("*.jpg"):
    print(file)
