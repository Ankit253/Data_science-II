import numpy as np
import matplotlib.pyplot as plt

print('#'*38,"Question 1:",'#'*38,'\n')
print('#'*40,"Part 1:",'#'*40)

N=10000 #N
X1 = np.random.randint(0,2,size=N) #Array X1
X2 = np.random.randint(0,2,size=N) #Array X2
print('\nThe number of times X1 takes the value 1:',sum(X1),'\t\t\tProbability:',sum(X1)/N)
print('The number of times X2 takes the value 1:',sum(X2),'\t\t\tProbability:',sum(X2)/N)

#Counting the events where both X1 and X2 are 1
Count = 0
for i in range(N): 
    if X1[i] == 1 and X2[i] == 1:
        Count+=1
print('The number of times both X1 and X2 take the value 1:',Count,'\tProbability:',Count/N)

print("\nProbability computed by hand:")
print('\nProbability that X1 takes the value 1:',1/2)
print('Probability that X2 takes the value 1:',1/2)
print('Probability that both X1 and X2 takes the value 1:',1/4)
print("\nX1 and X2 are independent\n")

print('#'*40,"Part 2:",'#'*40)
Z=X1+X2 #Z

print('\nThe number of times X1 takes the value 1:',sum(X1),'\t\t\tProbability:',sum(X1)/N)
print('The number of times Z takes the value 1:',sum(Z==1),'\t\t\tProbability:',sum(Z==1)/N)

#Counting the events where both X1 and Z are 1
Count = 0
for i in range(N):
    if X1[i] == 1 and Z[i] == 1:
        Count+=1
print('The number of times both X1 and Z take the value 1:',Count,'\tProbability:',Count/N)

print("\nProbability computed by hand:")
print('\nProbability that X1 takes the value 1:',1/2)
print('Probability that Z takes the value 1:',1/2)
print('Probability that both X1 and Z takes the value 1:',1/4)
print("\nX1 and Z are independent\n")

print('#'*40,"Part 3:",'#'*40,'\n')
P_X1_Z = 0   #P(X1=1 / Z=1)
P_X2_Z = 0   #P(X2=1 / Z=1)
P_X1_X2_Z=0  #P(X1=1, X2=1 / Z=1)

#Finding Relevent Probability 
Count_1=0
for i in range(N):
    if Z[i]==1:
        Count_1 += 1
        if X1[i] == 1 :
            P_X1_Z+=1
        if X2[i] == 1 :
            P_X2_Z+=1
        if X1[i] == 1 and X2[i] == 1 :
            P_X1_X2_Z+=1
P_X1_Z /= Count_1
P_X2_Z /= Count_1
P_X1_X2_Z /= Count_1

print('P(X1 = 1, X2 = 1|Z = 1) :',P_X1_X2_Z)
print('P(X1 = 1|Z = 1)P(X2 = 1|Z = 1):',P_X1_Z*P_X2_Z)

print("\nProbability computed by hand:")
print('P(X1 = 1, X2 = 1|Z = 1) :',0)
print('P(X1 = 1|Z = 1)P(X2 = 1|Z = 1):',1/2*1/2)
print('\nX1 conditioned on Z is dependent of X2 conditioned on Z\n')

print('#'*38,"Question 2:",'#'*38,'\n')

N = [1000]             #N
P = [0.25,0.5,0.75]    #P

#Simulation For Each N and P
for n in N:
    for p in P:
        arr = np.zeros(10000)
        for i in range(10000):
            arr[i]=sum(np.random.binomial(1,p,n)) #No. of Heads
        
        #Histogram
        plt.hist(arr)
        plt.xlabel('No. of Heads')
        plt.ylabel('Frequency')
        plt.title("N : "+str(n)+'\nP(H) : '+str(p))
        plt.grid()
        plt.show()

print('#'*38,"Question 3:",'#'*38,'\n')
P=[0.25,0.5,0.75]  #P
N=10000            #N

#Simulation For Each P
for p in P:
    arr = []
    for n in range(N):
        s = ''
        while ('1' not in s):
            x = np.random.random()
            if x <= p: s += '1'
            else: s += '0'
        arr.append(len(s)) #No. of attempts for Successful transmission
        
    bins = range(1,max(arr)+1) #Bins for Histogram
    #Histogram
    plt.hist(arr,bins=bins,align='mid')
    plt.ylabel("Frequency")
    plt.xlabel("No of attempts for successful transmission")
    plt.title('P(b = 1) = '+str(p))
    plt.grid()
    plt.show()
    