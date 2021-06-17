#%% Ques 1
import random
import matplotlib.pyplot as plt
import numpy as np


def die2coin(method_num, repetitions):

    if method_num == 1:
        lst = []
        while(repetitions > 0):
            d = random.randint(1, 6)
            if d == 1 or d == 2 or d == 3:
                lst.append("H")
            else:
                lst.append("T")
            repetitions -= 1
        return lst
    
    elif method_num == 2:
        lst = []
        while(repetitions > 0):
            d = random.randint(1, 6)
            if d == 1:
                lst.append("H")
            elif d == 2:
                lst.append("T")
            repetitions -= 1
        return lst
    
    elif method_num == 3:
        lst = []
        while(repetitions > 0):
            d = random.randint(1,100)
            if d % 2 == 0:
                lst.append("H")
            else:
                lst.append("T")
            repetitions -= 1
        return lst
    
    else:
        return "Invalid method number(1,2 and 3 exist)"
    
def count_heads_and_tails(givenlist):
    givenlist_heads_count = 0
    givenlist_tails_count = 0
    for element in givenlist:
        if element == "H":
            givenlist_heads_count += 1
        else:
            givenlist_tails_count += 1
    
    return givenlist_heads_count, givenlist_tails_count
    
    

list1 = die2coin(1,10000)
list2 = die2coin(2,10000)
list3 = die2coin(3,10000)

list1_heads_count, list1_tails_count = count_heads_and_tails(list1)
list2_heads_count, list2_tails_count = count_heads_and_tails(list2)
list3_heads_count, list3_tails_count = count_heads_and_tails(list3)

fig = plt.figure()


plt1 = fig.add_subplot(131)
plt2 = fig.add_subplot(132)
plt3 = fig.add_subplot(133)


plt1.bar(["H", "T"], [list1_heads_count, list1_tails_count])
plt2.bar(["H", "T"], [list2_heads_count, list2_tails_count])
plt3.bar(["H", "T"], [list3_heads_count, list3_tails_count])

plt.show()

#%% Ques 2

def die2BiasedCoin(repetitions):
    lst = []
    while(repetitions > 0):
        d = random.randint(1, 6)
        if d == 1 or d == 2 or d == 3 or d == 4:
            lst.append("H")
        else:
            lst.append("T")
        repetitions -= 1
    return lst


HT_list = die2BiasedCoin(10000)
HT_list_heads = 0
HT_list_tails = 0

for element in HT_list:
    if element == "H":
        HT_list_heads += 1
    else:
        HT_list_tails += 1


plt.bar(["H","T"],[HT_list_heads, HT_list_tails])
plt.show()


#%% Ques 3
import numpy as np
import matplotlib.pyplot as plt
import random

def solve(num_of_ppl):
    birthdays = []
    for i in range(num_of_ppl):
        Rand_Bday = random.randint(1,days_in_a_year)
        birthdays.append(Rand_Bday)

    common_Bdays = 0

    for ele in birthdays:
        if birthdays.count(ele) >= 2:
            common_Bdays += 1

    return common_Bdays

def scatterplot(x,y,days_in_a_year):
    plt.title("Common birthdays vs. Num of ppl")
    plt.xlabel("Num of ppl")
    plt.ylabel("Common Bdays")
    plt.scatter(x, y, color = 'green', marker = '*')
    plt.show()
    
def partC():
    num_of_ppl = np.arange(1, days_in_a_year+1)
    prob_list = []
    interval_arnd_fifty = int(input("Interval around 50 (5 means 45 to 55): "))
    days_under_consideration = 2*interval_arnd_fifty + 1
    
    for rep in range(100):
        y = []
        for val in num_of_ppl:
            y.append(solve(val))

        fav_cases = 0
        for day in range(49-interval_arnd_fifty,50+interval_arnd_fifty):
            if y[day] >= 2 :
                fav_cases += 1

        probability = fav_cases/float(days_under_consideration)
        prob_list.append(probability)

    avg_probability = sum(prob_list) / len(prob_list)
    print(avg_probability)
    



days_in_a_year = int(input("Days in a year: "))
num_of_ppl = np.arange(1, days_in_a_year+1)

x = np.arange(1, days_in_a_year+1)
y = []

for val in num_of_ppl:
    y.append(solve(val))

scatterplot(x, y, days_in_a_year)

partC()


y2 = []
days_in_a_year = 365
for i in range(days_in_a_year):
    if i < 150 :
        y2.append(2*y[i])
    else:
        y2.append(y[i])

scatterplot(x,y2,days_in_a_year)
    
#%%