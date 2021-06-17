#Q1

import math
import matplotlib.pyplot as plt

lam=57   #parameter(cases in hour)

def pdf(x):
    p=lam*math.e**(-lam*x)   #distribution of exponential fun.
    return p
def cdf(x):
    c=1-math.e**(-lam*x)   #cumulative distr. of exponential fun.
    return c

#A
X=[x/1000 for x in range(500)]
Y=[pdf(x) for x in X]

plt.plot(X,Y,linewidth=4,c='red')   #means next case will confirmed in few minutes 
plt.xlabel('Time(Hrs)')
plt.ylabel('PDF')
plt.show()


#B
print('\nProbability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute=')
print(cdf(1/60))


#C
print('\nProbability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes=')
print(cdf(2/60)-cdf(1/60))


#D
print('\nProbability of the wait time for the next Covid-19 confirmed case to be more than 2 minutes=')
print(1-cdf(2/60))


#E
lam*=2
print('\nProbability of wait time for the next Covid-19 confirmed case to be between 1minute and 2 minutes=')
print(cdf(2/60)-cdf(1/60))



#--------------------------------------------------------------------------------------------------------------

#Q2

import pandas as pd
file=pd.read_csv('IC252_Lab8.csv')


#A
status=list(file['Status'])

for i in range(len(status)):  #changing code for hospi , recovered, dead
    if status[i]=='Hospitalized':
        status[i]=1
    elif status[i]=='Recovered':
        status[i]=2
    else:         #dead
        status[i]=3

population=file['Population']
sexratio=file['SexRatio']
literacy=file['Literacy']
age=file['Age']
smelltrend=file['SmellTrend']
gender=file['Gender']


#B
def Mean(X):
    return(sum(X)/len(X))
    
def Covariance(X,Y):
    x_mean=Mean(X)
    y_mean=Mean(Y)
    covariance=0
    for i in range(len(X)):
        covariance+=(X[i]-x_mean)*(Y[i]-y_mean)
    covariance/=(len(X)-1)
    return covariance

def Stdev(X):
    x_mean=Mean(X)
    stdev=0
    for i in range(len(X)):
        stdev+=(X[i]-x_mean)**2
    stdev/=(len(X)-1)
    stdev=stdev**0.5
    return stdev
def Correlation(X,Y):
    correlation=Covariance(X,Y)/(Stdev(X)*Stdev(Y))
    return correlation

 #a
print('\nThe Correlation coefficient between Status and Population is:')
print(Correlation(population,status),'\n')
 #b
print('The Correlation coefficient between Status and SexRatio is:')
print(Correlation(sexratio,status),'\n')
 #c
print('The Correlation coefficient between Status and Literacy is:')
print(Correlation(literacy,status),'\n')
 #d
print('The Correlation coefficient between Status and Age is:')
print(Correlation(age,status),'\n')
 #e
print('The Correlation coefficient between Status and SmellTrend is:')
print(Correlation(smelltrend,status),'\n')
 #f
print('The Correlation coefficient between Status and Gender is:')
print(Correlation(gender,status),'\n')



#C
list1=['Status and Population','Status and SexRatio','Status and Literacy','Status and Age','Status and SmellTrend','Status and Gender']
list2=[Correlation(population,status),Correlation(sexratio,status),Correlation(literacy,status),Correlation(age,status),Correlation(smelltrend,status),Correlation(gender,status)]


for i in range(6):
    for j in range(6):
        if list2[i]>list2[j]:
            list2[i],list2[j]=list2[j],list2[i]
            list1[i],list1[j]=list1[j],list1[i]

for i in range(6):
    print(list1[i],':',list2[i])
print('\n'+'Conclusion: Age correlates strongly to the Status.\n(The correlation between Status and Age are Moderate and Weak with the rest.)')




        