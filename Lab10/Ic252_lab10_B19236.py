# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:57:14 2020

@author: B19236
"""

import numpy as np

def mont(con,n,a,b,A,B):   #con is a function and (a,b,A,B) is a fun of area (a-b)*(A-B)
    c=0
    X=np.around((b-a)*np.random.random(n)+a,decimals=3)   #generating n points on x axis
    Y=np.around((B-A)*np.random.random(n)+A,decimals=3)   #generating n points on y axis
    for x,y in zip(X,Y):    #zipping x and y as a points
        if eval(con):      #if point lie in the con
            c+=1
    return (c/n)*(b-a)*(B-A)

def dearr(n,s):  #sample of n array with each size of s
    c = n
    array = [np.random.permutation(range(1, s+1)) for i in range(n)]   #n random arrays of size s
    for arr in array:
        for x in range(s):
            if arr[x] == x + 1:     #property for arranged array
                c -= 1      #number of dearranged array
                break
    return n/c   # (n!/!n)=e

print("ques.1")
for n in [100,1000,10000]:
    print(f"\tπ ≈ {mont('x**2+y**2<=1',n,-1,1,-1,1)}, for n={n}")    #circle of r=1 and square of area 2

print("ques.2")      
for n in [100,1000,10000]:
    print(f"\t∫f(x)dx ≈ {mont('y- 2/(1+(x**2)) <= 0',n,0,1,0,2)}, for n={n}") 

print("ques.3")
for n in [100,1000,5000,10000]:
    print(f"\te ≈ {round(dearr(n,50),5)}, for n={n}")  #rounding value of e upto 5 decimal