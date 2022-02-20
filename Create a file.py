#Scott Larrentree    

import json
import os

print("Where do you want to save your file? : ")
userDir = input()

if os.path.isdir(userDir):
    print("\nPath was found!")
else:
    os.mkdir(userDir)
    print("\nPath not found! New path being created.")

os.chdir(userDir)

userFile = input("\nWhat is the name of the file you like to create? \n")
userName = input("\nWhats your name?\n")
userAddress = input("\nWhat is you address?\n")
userPhone = input ('\nWhat is your phone number\n')



fileName = f'{userFile}.txt'
with open(fileName, 'w') as f:
    f.write(f'{userName}, {userAddress}, {userPhone}')

with open(fileName, 'r') as f:
    for line in f:
        print(line)
