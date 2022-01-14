

1-QUESTION:Write a calculator function which takes orderly first number, operator and second number than gives the result.

def calculator():
    operation=input().split()
    a,o,b=int(operation[0]),operation[1],int(operation[2])
    
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/':
        return a/b
    else:
        return ('Please enter a valid operator sign')

calculator()



2-QUESTION:Write a function that calculates factorial of a given number.

def my_fact(n):
    if n<=1:
        return 1
    result=n*my_fact(n-1)
    return result

print('The factorial equals: {}'.format(my_fact(4)))

3-QUESTION:This is an interview question asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

 [34, -50, 42, 14, -5, 86]

def subarray(arr):
    total=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if sum(arr[i:i+j+1])>total:
                total=sum(arr[i:i+j+1])
    print(total)

subarray([34, -50, 42, 14, -5, 86])

#alternative solution from Hamza
def subarray_finder(liste):
    if sum(liste)>0:
        newlist = []
        count = 0
        for i in range(len(liste)):
            sayı = sum(liste[i:len(liste)])
            sayı1 = sum(liste[len(liste)-count:i:-1])
            newlist.append(sayı)
            newlist.append(sayı1)
            count +=1
        return max(newlist)
    else:
        return 0

subarray_finder([34, -50, 42, 14, -5, 86])

4-QUESTION: Interview Level = Medium
    
Given a string s, find the length of the longest substring without repeating characters.


def lengthOfLongestSubstring(s):
    smax,temp='',''
    for i in s:
        if i in temp:
            if len(temp)>len(smax):
                smax=temp
            while i in temp:
                temp=temp[1:]
        temp+=i
#     if smax:
#         return smax, len(temp)
#     else: 
#         return temp, len(temp)
    return (smax*(len(smax)>len(temp))+temp*(1-(len(smax)>len(temp))), max(len(smax),len(temp)))

lengthOfLongestSubstring('abcbdhhgfd')

# alternative solution from Yusuf
def substring(text:str):
    long = ""
    for i in range(len(text)):
        temp = ""
        for j in range(i, len(text)):
            if text[j] in temp:
                break
            temp += text[j]
        if len(temp) > len(long): #takes first one
#       if len(temp) >= len(long): takes last one 
            long = temp
    return long, len(long)

substring('abcbdhhgfd')

5.QUESTION:Create your own module named as my_module.py which contains a function printing Hello 'Your Name' when called. 
Also create a dictionary object which keeps name and profession of you inside your module. Finally put the calculator function 
in your module and call it with both import from your interpreter and from your command prompt. 

import mymodule

mymodule.my_function()

mymodule.person

mymodule.person['profession']

mymodule.calculator2()



import numpy as np

np.max([34, -50, 42, 14, -5, 86])

import pandas as pd



6. QUESTION:Use the calculator you created before and name it as calculator2. Implement Full 'Exception Handling' while callling calculator2. Try to run your function, if exception occurs write 'Please enter a valid operator and valid number values' and finally write 'Calculator works just fine' for every run.

def calculator():
    operation=input().split()
    a,o,b=int(operation[0]),operation[1],int(operation[2])
    
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/':
        return a/b
    else:
        return ('Please enter a valid operator sign')

try:
    result=calculator()
    print(result)
except:
    print('Please enter valid values')
finally:
    print('Calculator works just fine')

try:
    result=calculator()
    print(result)
except ZeroDivisionError:
    print('Nominator is zero please change it')
finally:
    print('Calculator works just fine')

