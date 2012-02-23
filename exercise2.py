import numpy
import inputdata
from math import sqrt
from scipy.stats.stats import pearsonr
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
            dist+=pow((vec1[p]-vec2[p]),2)
    norm=sqrt(dist)
    return norm

def pearson_corr(guy1,guy2):
    vec1=ratings[guy1]
    vec2=ratings[guy2]  
    l1=list()
    l2=list()
    for p in range(len(papers)):
            if vec1[p]!=0. and vec2[p]!=0.: 
                l1.append(vec1[p])
                l2.append(vec2[p])  
   # print "l1 " + str(l1)
    #print "l2 " + str(l2)
   # print "pearson " + str(numpy.cov(numpy.array(l1), numpy.array(l2)))
    return pearsonr(numpy.array(l1), numpy.array(l2))[0]


mutual_norms=numpy.zeros((len(people),len(people))) 
pearson_norms=numpy.zeros((len(people),len(people))) 

for n in range(len(people)):
      for m in range(len(people)):
           if n==m:
              pearson_norms[n][m]=1.
              mutual_norms[n][m]=100.
           else:
              mutual_norms[n][m]=norm2(n,m)
              pearson_norms[n][m]=pearson_corr(n,m)

print "mutual norms"       
print mutual_norms
print "Pearson correlations"
print pearson_norms

for n in range(len(people)):
       print "Similar researchers as " + str(people[n]) + "are: "
       for p in range(5):       
           m=numpy.where(mutual_norms[n]==numpy.min(mutual_norms[n]))
           print people[m[0][0]]
           mutual_norms[n][m[0][0]]=numpy.max(mutual_norms[n])
  


