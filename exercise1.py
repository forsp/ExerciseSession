import os
import fileinput

fold="cleaneddata"


def listfiles(dir):
    return os.listdir(dir)

def findmiss(file):
    for line in fileinput.input(file):
            array=line.split(":")
            if len(array)==2 and array[1].strip()=="N":
            return True
            else:
            return False

def main():
    #print listfiles(fold)
    for file in listfiles(fold):
        print str(file) + ':' +str(findmiss(file))

main()

    
