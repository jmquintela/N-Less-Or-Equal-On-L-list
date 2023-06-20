import time
from random import randrange

import numpy as np


def nearestEqualOrSmallerIndex(n:int, indexSlicers, initialL, debug=False):
  
  n2 = 0
  l = initialL[indexSlicers[0]:indexSlicers[1]]
  
  if debug:
      
      print("index Slicers: {} \n n : {} \n ".format(indexSlicers,n))     
  
  for x,v in enumerate(l):
  
    IfEqual = (v == n)
    IfLess = (v < n)
    IfBigger = (v > n)

    index = indexSlicers[0] + x 
        
    if debug:
      
      conditions = []
      v2 = initialL[index]  
      conditions.append(IfEqual)
      conditions.append(IfLess)
      conditions.append(IfBigger)
      
      print("conditions : {} \n\n n: {} \n x: {} \n index: {} \n value loop: {} \n value on list: {} ".format(conditions,n,x,index,v,v2))   
   
    if IfEqual:
        n2 = index 
        break
    if IfLess:
        #we append the index of the values
        n2 = index  
        
    if IfBigger:
        n2 = index-1    
        break  
  if debug:
      print("n final: {} ".format(n2))  
 
  return n2
  #Give us the last appenden object 
       
def equalOrSmallerIndexOnListToN(n:int, l:list, debug=False):  
  
    # l is a sorted list
    
    lenL = len(l)
    leftSlice = 0
    rightSlice = lenL
    indexSlicers=[leftSlice,rightSlice]
    initialL = l
    d = 100
    
    def findIndex(d:int,n:int,lenL:int,indexSlicers:list, initialL:list,debug=False) -> list:
             
      ifNBiggerThanlenL = ( initialL[-1] <= n)    
      if ifNBiggerThanlenL:    
        return lenL-1         
      ifLenNLessorEqualltoD = (lenL <= d)
     
      if  ifLenNLessorEqualltoD:    
        #we short the loop when we reach d element        
        return nearestEqualOrSmallerIndex(n,indexSlicers,initialL,debug)          
      
      #We pick a random position on this range  
      
      div = 15
      part = int(lenL / div)   
      N = list(range(0,div,1))
      maxL = len(initialL)
      for i in N:
        
        random1 = int(randrange(1,part,1)) 
        #print(i)
        
        i = (i-1)*part
       
        #print("i : {}".format(i))
        #print("random : {}".format(random))
        
        random = indexSlicers[0]+ i+random1
        #with this we max the value of random so it soesnt outbound the list
        if random >= maxL:
          random = maxL -1
        if debug: 
         print("part:{} \n , i : {} \n , random1 : {} \n lenL = {}".format(part,i,random1,lenL))
        # print(len(initialL))
        #print(len(N))
        v = initialL[random]
        
        #print("value: {}".format(v))
        #print(v)
        
        if v == n :
          return random
        if v < n : 
          if random > indexSlicers[0]: 
           indexSlicers[0] = random  
          #print("slicer down : {} \n".format(indexSlicers[0]))
        if v > n :
          if random < indexSlicers[1]: 
           indexSlicers[1] = random
          #print("slicer up : {} \n".format(indexSlicers[1]))    
        
      lenL = indexSlicers[1] - indexSlicers[0]
      #print("lenL {} \n".format(lenL))
      return findIndex(d, n, lenL, indexSlicers, initialL, debug )    
    
    
    return findIndex(d, n, lenL, indexSlicers, initialL, debug )
   
n2 = 100022235
n = 359443

l = list(range(0,n2,3))  
debug=True
prime_tic = time.perf_counter()  
i = EqualorSmallerIndexOnListToN(n,l,debug)
prime_toc = time.perf_counter()  
runTime = prime_toc - prime_tic

print("runtime : {} seconds".format(runTime))

print("the value on index  {} is: {}".format(i,l[i]))
