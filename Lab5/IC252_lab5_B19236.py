#Q1(a)

from random import randint
from random import random
import numpy as np

x = []
y = []

#p = int(input())
#q = int(input())
p = 0.25
q = 0.35 
for i in range(10000):
    temp = randint(0,1)
    x.append(temp)
    
    
def x1():
    temp = random()
    if temp >= q:
        return 1
    else:
        return 0

    
def x0():
    temp = random()
    if temp >= p:
        return 0
    else:
        return 1
    
for i in x:
    if i == 1:
        y.append(x1())
    else:
        y.append(x0())
        
counts = np.zeros((2,2))

for i in range(10000):
    if x[i] == 0  and y[i] == 0:
        counts[0][0]+=1
    if x[i] == 1  and y[i] == 0:
        counts[0][1]+=1
    if x[i] == 0  and y[i] == 1:
        counts[1][0]+=1
    if x[i] == 1  and y[i] == 1:
        counts[1][1]+=1

mpdf = counts/10000

import pandas as pd

dfc = pd.DataFrame(counts)
dfPDF = pd.DataFrame(mpdf)

import matplotlib.pyplot as plt

dataset = pd.DataFrame({'X' : (0,1,0,1), 'Y' : (0,0,1,1), 'Z' : list(counts[0]) + list(counts[1])})

from mpl_toolkits.mplot3d import Axes3D #for 3D projection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dataset['X'], dataset['Y'], dataset['Z'], c='k', s=100)
ax.view_init(30, 185)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Counts")
ax.set_title("Simulation Results")
plt.show()


#Q2(a)


pdf = pd.DataFrame({'X' : (0,1,0,1), 'Y' : (0,0,1,1), 'Z' : list(mpdf[0]) + list(mpdf[1])})

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pdf['X'], pdf['Y'], pdf['Z'], c='k', s=100)
ax.view_init(30, 185)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Probability")
ax.set_title("PDF")
plt.show()

#verifying results
#1(b)
print('P(Y=0) = ', (mpdf.sum(0)[0]))
print('P(Y=1) = ', (mpdf.sum(0)[1]))

#2(b)
print('P(Y=0|X=0) = ', mpdf[0][0]/(mpdf.sum(0)[0]))
print('P(Y=0|X=1) = ', mpdf[1][0]/(mpdf.sum(0)[0]))
print('P(Y=1|X=0) = ', mpdf[0][1]/(mpdf.sum(0)[1]))
print('P(Y=1|X=1) = ', mpdf[1][1]/(mpdf.sum(0)[1]))
