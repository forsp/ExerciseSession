import os
import fileinput

fold="cleaneddata"


def listfiles(dir):
    return os.listdir(dir)

def findmiss(file1):
      #for line in file1.readlines():
        line=file1.readlines()
        if "Sex: N\n" in line:
                 return True
        else:
                return False 
  
def main():
   # print listfiles(fold)
 #   for file1 in listfiles(fold):
       file1=open('cleaneddata/jamesm_data_360.txt')
       print str(file1) + '-' +str(findmiss(file1))

main()

    
