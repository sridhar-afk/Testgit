# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:22:04 2020

@author: AJ
"""
#Convert List into String
test = ['Hello', 'World', '!']
string_val = ' '.join(test)

#Print Count of values in list
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
ans = [[x,weekdays.count(x)] for x in set(weekdays)]

#Negative indexing
a = [1,2,3,4,5]

#Index
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names3 = names1[:]

#Reversal of number
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number % 10
    print(Reminder)    
    Reverse = (Reverse * 10) + Reminder
    print(Reverse)    
    Number = Number // 10  
    print(Number)

#Pattern Progranm 1
num = 4
for i in range(0,num):
    for j in range(0, num-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print('\n')
    
#Pattern Progranm 2
num = 5
for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print('\n')

#sample list program    
def extend(val, list = []):
     list.append(val)
     return list

list1 = extend(10)
list2 = extend(123, [])
list3 = extend('a')