#!/usr/bin/python
import sys
import os,time
import datetime



MAX_AGE_IN_DAYS=5
counter=0

if len(sys.argv)!=2:
    print("Check provided arguments.")
    sys.exit(0)

path=sys.argv[1]
try:
    os.chdir(path)
except OSError:
    print("Could't access selected path. Closing script")
    sys.exit(0)

listOfFiles=os.listdir(".")
filteredListOfFiles=[]
for file in listOfFiles:
    if ".mkv" in file:
        filteredListOfFiles.append(file)

today = datetime.datetime.now()

for file in filteredListOfFiles:
    dt=datetime.datetime.fromtimestamp(os.path.getctime(file))
    delta=today-dt
    if delta.days>MAX_AGE_IN_DAYS:
        os.remove(file)
        counter=counter+1
    
print ("Deleted "+str(counter)+" videos")



