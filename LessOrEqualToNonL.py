import time
from random import randrange

import numpy as np


def nearestEqualOrSmallerIndex(n:int, indexSlicers, initialL, debug=False):
  n2 = 0
  l = initialL[indexSlicers[0]:indexSlicers[1]]
  if debug:
      print("index Slicers: {} \n\n l: {} \n\n n : {} \n\n ".format(indexSlicers,l,n))     
  
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
       
def EqualorSmallerIndexOnListToN(n:int, l:list, debug=False):  
    # l is a sorted list
    lenL = len(l)
    leftSlice = 0
    rightSlice = lenL
    indexSlicers=[leftSlice,rightSlice]
    initialL = l
    d = 50
    
    def FindNearNumberbyHalfingSignComparison(d:int,n:int,lenL:int,indexSlicers:list, initialL:list,debug=False) -> list:
             
      ifNBiggerThanlenL = ( initialL[-1] <= n)    
      if ifNBiggerThanlenL:    
        return lenL-1        
      ifLenNLessorEqualltoD = (lenL <= d)
       
      if  ifLenNLessorEqualltoD:    
        #we short the loop when we reach d element        
        return nearestEqualOrSmallerIndex(n,indexSlicers,initialL,debug)          
      
      #We pick a random position on this range  
                       
      random = int(randrange(lenL-1))
      
      index = indexSlicers[0] + random
      value = initialL[index] 
      conditions=[]
       
      IfBigger = (n > value)
      IfEqual = (n == value)
      IfLess = (n < value)
      
      conditions.append(IfBigger)
      conditions.append(IfEqual)
      conditions.append(IfLess)
      
      if debug:
       print( "lenL : {}, n: {} \n Conditions: {} \n Value :  {}\n Index :  {}  \n Slicing index : {} \n".format(lenL,n,conditions,value,index,indexSlicers) )
  
      if IfEqual:
    
         return  index
        
      if IfBigger:
        
         indexSlicers[0] = index          
         l = initialL[indexSlicers[0]:indexSlicers[1]]
         lenL = len(l)
         
         return FindNearNumberbyHalfingSignComparison(d,n, lenL,indexSlicers, initialL, debug )
      
      #and slice the parts from the array that are   

      if IfLess:
         indexSlicers[1] = index                   
         l = initialL[indexSlicers[0]:indexSlicers[1]]
         lenL = len(l)
         return FindNearNumberbyHalfingSignComparison(d,n , lenL ,indexSlicers, initialL, debug)
      
      
    return FindNearNumberbyHalfingSignComparison(d, n, lenL, indexSlicers, initialL, debug )
   
n2 = 100022235 #list end number
n = 359443 #number on the list

l = list(range(0,n2,3))  
debug=True
prime_tic = time.perf_counter()  
i = EqualorSmallerIndexOnListToN(n,l,debug)
prime_toc = time.perf_counter()  
runTime = prime_toc - prime_tic

print("runtime : {} seconds".format(runTime))

print(l[i])
