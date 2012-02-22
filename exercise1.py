import os, glob
import fileinput

fold="cleaneddata"


def listfiles(dir):
    return os.listdir(dir)

def findmiss(file1):
      
        line=open(file1).readlines()
        if "Sex: N\n" in line:
                 return True
        else:
                return False 

def changeNM(file1):
        line=open(file1).read()
        line=line.replace(': N',': M')
        print 'Changing N to M in '+file1
        file2 = open(file1,'w')
        file2.write(line)
        file2.close()
  
def main():
   # print listfiles(fold)
    os.chdir(fold)
    n=0
    for file1 in glob.glob('*.txt'):
        #      print str(file1) + '-' +str(findmiss(file1))
        if findmiss(file1):
            changeNM(file1)
            n+=1
    print "Done! " + str(n) + " changes made"
main()

    
