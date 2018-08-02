#!/usr/bin/python
import sys
import os,time
import datetime

VIDEO_EXTENSION=".mkv"
MAX_AGE_IN_DAYS=5

def chechArguments():
    if len(sys.argv)!=2:
        print("Check provided arguments.")
        sys.exit(0)

def openPath(path):
    try:
        os.chdir(path)
    except OSError:
        print("Could't access selected path. Closing script")
        sys.exit(0)

def getVideos():
    listOfFiles=os.listdir(".")
    filteredListOfFiles=[]
    for file in listOfFiles:
        if VIDEO_EXTENSION in file:
            filteredListOfFiles.append(file)
    return filteredListOfFiles

def deleteOldVideos(fileList):
    today = datetime.datetime.now()
    for file in fileList:
        fileCreationDate=datetime.datetime.fromtimestamp(os.path.getctime(file))
        delta=today-fileCreationDate
        if delta.days>MAX_AGE_IN_DAYS:
            os.remove(file)

chechArguments()
path=sys.argv[1]
openPath(path)
videos=getVideos()
deleteOldVideos(videos)   
print ("Deleted videos")



