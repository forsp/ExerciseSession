import numpy
import inputdata
from math import sqrt
data = inputdata.raw_scores

class Rating(object):
  
      def __init__(self):
        self.ratings=nympy.array([],dtype='f')
        self.ratings.reshape(0,2)
        self.people=[]
        self.papers=[]


people=data.keys()
papers=list()

for n in range(len(people)):
    for paper_name, value in data.values()[n].iteritems(): 
          papers.append(paper_name)
        
set_of_papers=set(papers)
papers=list(set_of_papers)


ratings=numpy.zeros((len(people),len(papers)))
   
for n in range(len(people)):
    for paper_name, value in data.values()[n].iteritems(): 
                for p in range(len(papers)):
                     # print papers[p]
                       if papers[p]==paper_name:          
                           ratings[n][p]=value

print ratings

def norm2(guy1,guy2):
    vec1=ratings[guy1]
    vec2=ratings[guy2]
    dist=0.    
    for p in range(len(papers)):
         if vec1[p]!=0. and vec2[p]!=0.:
            dist+=(vec1[p]-vec2[p])**2 
    norm=sqrt(dist)
    return norm

mutual_norms=numpy.zeros((len(people),len(people))) 
for n in range(len(people)):
      for m in range(len(people)):
         #  if n==m:
          #    mutual_norms[n][m]=
        #   else:
              mutual_norms[n][m]=norm2(n,m)
       
print mutual_norms

