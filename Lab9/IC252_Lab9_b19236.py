#ankit B19236 lab9

#============================================================================

#QUESTION-1

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sc
from scipy.stats import bernoulli

def mean(array):
    return sum(array)/len(array)
m =[10,50,100,500,1000,5000,10000]  #random datasets of size m

class generator():
    def _init_(self):
        pass
        
    def exponential(self, size): 
        ans =[]
        
        temp = np.random.exponential(1,size)   #exponential distrbted r.v. with lambda 1
        for i in temp:
            ans.append(round(i,1))   #asked to round of number to 1 decimal
        return ans
    
    def uniform(self,size):
        ans =[]
        temp = np.random.uniform(1,2,size)   #uniformly dist. rv b/w 1 & 2
        for i in temp:
            ans.append(round(i,1)) #round of to 1 decimal
        return ans
    
    
    def bernoulli(self,size):  #size = n
        ans =[]
        for i in range(size):
            ans.append(bernoulli.rvs(0.2))  
        return ans
    
bern =[]
unif =[]
exp =[]
g =  generator()

for i in m:   #i is size
    exp.append(mean(g.exponential(i)))   #mean of m exp r.v. (=1/lambda=1)
    bern.append(mean(g.bernoulli(i)))    #mean of m bernoulli r.v. (=p=0.2)
    unif.append(mean(g.uniform(i)))      #mean of m uniform r.v. (=a+b/2=1.5)
    
X = m
Y = [exp[i] for i in range(len(m))]
Y1 = [bern[i] for i in range(len(m))]
Y2 = [unif[i] for i in range(len(m))]
plt.plot(X,Y,label ="exponential distribution")
plt.plot(X,Y1,label = "bernoulli distribution")
plt.plot(X,Y2,label = "uniform distribution")
plt.grid(True)
plt.xlabel("sample size")
plt.ylabel("sample mean")
plt.title("WLLN For Different Distributions")
plt.legend()
plt.show()

#=============================================================================================================

#QUESTION-2


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sc

for j in [("Exponential",1,1),("Uniform",1.5,1/12),("Binomial",0.2,0.2*0.8)]:
    L=[]
    if j[0]=="Exponential":  #exp. lambda=1, sample mean(x-axis)=[0,4], E(X)=1/lambda=1
        for n in range(32):
            L.append(np.random.exponential(1,size=1000))  #generating 1000 samples of exp r.v.
        x=np.linspace(0,4,51)
        bins=np.linspace(0,4,101)
        width=1/25
    elif j[0]=="Uniform":    #uniform dist. b/w [1,2] --> sample mean(x-axis)=[1,2], E(X)=a+b/2=1.5
        for n in range(32):
            L.append(np.random.uniform(1,2,size=1000))
        x=np.linspace(1,2,51)
        bins=np.linspace(1,2,101)
        width=1/100
        
    else:                   #binomial with p=0.2, sample mean(bernoulli dist.)=[0,1], E(X)=p
        for n in range(32):
            L.append(np.random.binomial(1,.2,size=1000))
        x=np.linspace(0,1,101)
        bins=np.linspace(0,1,21)
        width=1/20
    
    for i in ([1,2,4,8,16,32]):  #number of Xi
        Y=np.linspace(0,0,1000)
        for n in range(i):
            Y+=np.array(L[n])
        Y=Y/i            
            
        histogram,bins=np.histogram(Y,bins=bins,density=True)
        bin_centers=(bins[1:]+bins[:-1])/2
        
        plt.figure(figsize=(8,6))
        plt.bar(bin_centers,histogram,width=width, alpha=0.8)
        
        mu=j[1]
        variance=(j[2]/i)
        plt.plot(x, sc.norm.pdf(x,mu,variance**0.5))
        plt.show() 