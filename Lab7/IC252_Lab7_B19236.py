
def sampleMean(X):
    sumofXi = 0;
    for Xi in X:
        sumofXi += Xi
    return sumofXi/len(X)

def sampleVariance(X):
    EX = sampleMean(X)
    sum1 = 0
    for Xi in X:
        sum1 += ((Xi-EX)**2)
    return sum1/(len(X)-1)

def sampleCovariance(X,Y):
    EX = sampleMean(X)
    EY = sampleMean(Y)
    sum1 = 0
    for i in range(len(X)):
        sum1 += (X[i]-EX)*(Y[i]-EY)
    return sum1/(len(X)-1)

def sampleCorrelation(X,Y):
    return sampleCovariance(X,Y)/((sampleVariance(X)*sampleVariance(Y))**0.5)

def Rel(P1,P2):
    X = data[P1]
    Y = data[P2]
    r = sampleCorrelation(X,Y)
    print("pearson Correlation coffecient between",P1,"and",P2,"=",r)
    print("Relationship between",P1,"and",P2,"is",Relationship(r))
    
def Relationship(r):
    r = abs(r)
    l1 = [0,0.1,0.3,0.5,1]
    l2 = ["None","Weak","Moderate","Strong","Very Strong","Perfect"]
    for i in range(len(l1)-1):
        if(r == 0):
            return l2[0]
        if(r >= l1[i] and r < l1[i+1]):
            return l2[i+1]
    return l2[len(l2)-1]
    
##Q1,Q2
X = [15,17,20,21,25]
Y = [9,13,16,18,21]
print("Covariance is ",sampleCovariance(X,Y))
print("Correlation is ",sampleCorrelation(X,Y))

##Q3
import pandas as pd
data = pd.read_csv("BNG-Device.csv")
data["Total-Memory-Usage"] = data["Total-Memory-Usage"].fillna(0)
P1 = "Active-Count"
P2 = "CPU-Utilization"
P3 = "Total-Memory-Usage"
P4 = "Average-Temperature"
Rel(P2,P1)
Rel(P2,P3)
Rel(P2,P4)
Rel(P1,P4)
Rel(P3,P4)
