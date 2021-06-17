#lab6.1

# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def graph(A, caption):    #function for PMF, A is age
    D={}        #dictionary with key as age and value as no. of person with that age 
    for i in A:       
        if i in D.keys():  
            D[i]+=1    #updating no. of person of that age 
        else:
            D.update({i:1})   #if that age is not in dict, add that
    
    for i in range(0, max(D.keys())):  #making age cont. in range
        if i not in D.keys():
            D.update({i:0})   #adding that age with 0 person
            
    
    L=[x[1] for x in sorted(D.items())] #no. of person of that age
    n=sum(L)      #total persons
    plt.bar(list(range(0,max(D.keys())+1)),np.array(L)/n)  #L/n is prob.
    plt.title(caption)
    plt.xlabel("Age")
    plt.ylabel("No. of patients")
    plt.show()


s=pd.read_excel("Covid19IndiaData_30032020.xlsx")

print("\nPart 1:")

A=s["Age"]
graph(A,"PMF of age of COVID-19 infected patients")
print("The expected age of a COVID-19 infected patient is about", round(A.mean(),3), "yrs.")
print("The variance of the PMF is about", round(A.var(),3), "yrs squared.")
print("\nThus, in light of this high value of variance, we can deduce that COVID-19 disease is quite independent of the age of the patients.")

print("\n\nPart 2:")

R=s[s["StatusCode"]=="Recovered"]
A=R["Age"]
graph(A, "PMF of age of recovered COVID-19 patients")

print("The expected age of a recovered COVID-19 patient is about", round(A.mean(),3), "yrs.")
print("The variance of the PMF is about", round(A.var(),3), "yrs squared.")

E=s[s["StatusCode"]=="Dead"]
A=E["Age"]
graph(A,"PMF of age of deceased COVID-19 patients")

print("The expected age of COVID-19 patient, who died due to COVID-19 is about", round(A.mean(),3), "yrs.")
print("The variance of the PMF is about", round(A.var(),3), "yrs squared.")
print("\nHence, by this analysis, we see that a middle-aged person has a greater chance of recovery, while elderly people are more prone to death by this disease.")

print("\nPart 3:")

M=s[s["GenderCode0F1M"]==1]
A=M["Age"]
graph(A, "PMF of age of male COVID-19 patients")

print("The expected age of a male COVID-19 patient is about", round(A.mean(),3), "yrs.")

F=s[s["GenderCode0F1M"]==0]
A=F["Age"]
graph(A, "PMF of age of female COVID-19 patients")

print("The expected age of a female COVID-19 patient is about", round(A.mean(),3), "yrs.")
print("\nHence, we can't infer any practical or proper conclusion from the analysis of this data, as it has too many females of the same age (38) infected.")
print("As far as real studies are concerned, there is hardly any difference in no. of infected patients of both genders. It is to be noted however, that some studies have shown a higher fatality rate for males.")




#lab6.2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def pmf(L,caption):   # function for pmf, L is incP
    D={}
    for i in L:        
        if str(i.days)!='nan':
            if i.days in D:
                D[(i.days)]+=1
            else:
                D.update({(i.days):1})
    X=[]
    Y=[]
    n=sum(D.values())
    for i in sorted(D.keys()):
        X.append(i)
        Y.append(D[i]/n)
    
    plt.bar(X,Y)
    plt.title(caption)
    plt.xlabel("No. of days")
    plt.ylabel("Probability")
    plt.show()
    #return sum(np.array(X)*np.array(Y))
    
xl=pd.ExcelFile("linton_supp_tableS1_S2_8Feb2020.xlsx")
surv=xl.parse("TableS1", header = 1, index_col=0)
dece=xl.parse("TableS2", header = 1, index_col=0)

expl=surv["ExposureL"]          #date of infection
expr=surv["ExposureR"]
expt=surv["ExposureType"]
onse=surv["Onset"]    #onset of symptoms
hosp=surv["DateHospitalizedIsolated"]
l=len(expl)

print("Part 2-1:")
IncP=[]         #incubation period
for i in range(l):
    if str(onse[i])!="NaT":   #if value is not empty
        if str(expl[i])!="NaT":   #if not empty
            IncP.append(onse[i]-expl[i])     #appending inc periods
            
pmf(IncP,"PMF of Incubation period")   #finding PMF



print("Part 2-2:")

IncPnW=[]            #incubation period excludig wuhan
for i in range(l):
    if str(expt[i])!="Lives-works-studies in Wuhan" and str(onse[i])!="NaT" and str(expl[i])!="NaT":
        IncPnW.append(onse[i]-expl[i])   #appending Periods

pmf(IncPnW,"PMF of Incubation period for non-Wuhan residents")   #PMF excluding Wuhan


print("Part 2-3:")
X=dece["Death"]
O=dece["Onset"]
H=dece["Hospitalization/Isolation"]

pmf(H-O,"PMF of onset to hospitalization for deceased.")
pmf(X-O,"PMF of onset to death")
pmf(X-H,"PMF of hospitalization to death")
print("Hence, we see a similar form of distribution in all three graphs, that they rise till a point, and then fall down towards zero, like a normal distribution.")

pmf(hosp-onse,"PMF of onset to hospitalization for survivors")
print("We can see that the most survivors were hospitalized soon after the onset of symptoms, while most of the deceased got hospitalized after some days. Hence, we can say that late treatment can lead to death by COVID-19.")

