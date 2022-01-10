<h1><center>Python Workshop - 30.11.2021</center></h1>

### Question 1
```
Write a function that returns True if every consecutive sequence of ones is followed by a consecutive sequence of zeroes of the same length.

same_length("110011100010") ➞ True

same_length("101010110") ➞ False

same_length("111100001100") ➞ True

same_length("111") ➞ False
```

num = "111100001100"

while '10' in num or '01' in num:
    num = num.replace('10', '').replace('01', '')
if num == '':
    print('True')
else:
    print('False')

### Question 2
```
Write a function that groups a string into parentheses cluster. Each cluster should be balanced.
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
```

num = "((()))(())()()(()())"

left, right = 0, 0
summ = ''
res = []

for i in num:
    if i == '(':
        left += 1
        summ += i
    else:
        right += 1
        summ += i
    if left == right:
        res.append(summ)
        left = 0
        right = 0
        summ = ''
print(res)

### Question 3
```
Create a function that returns a list containing the prime factors of whatever integer is passed to it.

prime_factors(20) ➞ [2, 2, 5]

prime_factors(100) ➞ [2, 2, 5, 5]

prime_factors(8912234) ➞ [2, 47, 94811]
```

num = 8912234
x = 2
res = []

while num > 1:
    if num % x == 0:
        num = num // x
        res.append(x)
    else:
        x += 1
print(res)

### Question 4
```
Create a function that takes a number num and returns each place value in the number.

num_split(39) ➞ [30, 9]

num_split(-434) ➞ [-400, -30, -4]

num_split(100) ➞ [100, 0, 0]
```

num = -45637
if num < 0:
    negative = True
    num = abs(num)
else:
    negative = False

res = []
num = str(num)
leng = len(num) - 1

for i in num:
    res.append(i + '0' * leng)
    leng -= 1

if negative:
    res = [-int(i) for i in res]
else:
    res = [int(i) for i in res]

print(res)

### Question 5
```
Create a function that takes an integer n and returns the factorial of factorials. 

See below examples for a better understanding:

fact_of_fact(4) ➞ 288
#4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200
```

n = 5

res = 1

for i in range(2, n + 1):
    num = 1
    for j in range(1, i + 1):
        num *= j
#         print('1',num)
    res *= num
#     print('2',res)
print(res)

### Question 6
```
You are given a list which may contain sublists. Your task is to find the depth of the deepest sublist.

[a] = 1 depth
[[a]] = 2 depth
[[[a]]] = 3 depth, etc
Examples
deepest([1, [2, 3], 4, [5, 6]]) ➞ 2

deepest([[[[[[[[[[1]]]]]]]]]]) ➞ 10

deepest([1, 4, [1, 4, [1, 4, [1, 4, [5]]]]]) ➞ 5
```

lst = [[],[[[[[5]]]]],[[[[[[[6]]]]]]],[[[[[[[[[[[[7]]]]]]]]]]]]]

lst = str(lst)

count = 0
res = []

for i in lst:
    if i == '[':
        count += 1
        res.append(count)
    elif i == ']':
        count -= 1
        res.append(count)
# print(res)
print(max(res))

### Question 7
```
"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

For n = 5: 
Loves me, Loves me not, Loves me, Loves me not, LOVES ME
```

n = 10

text = 'Loves me'
res = ''
for i in range(1, n + 1):
    if i % 2 == 0:
        a = text + ' not, '
    else:
        a = text + ', '
    if i != n:
        res += a
    else:
        res += a.upper()
res = res.rstrip(', ')
res

### Question 8
```
Given a string of size n, write functions to perform following operations on string.
Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n). 
For example given word: "Hippopotamus"  

result =
Left Rotation :  opotamusHipp
Right Rotation :  amusHippopot
```

n = 5

text = 'Hippopotamus'

left = text[n:] + text[:n]
right = text[:-n-1:-1][::-1] + text[:len(text) - n]

print(left)
print(right)

### Question 9
```
Given two strings s and t, create a function to determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Examples
is_isomorphic("egg", "add") ➞ True

is_isomorphic("aba", "baa") ➞ False

is_isomorphic("paper", "title") ➞ True
```

x = 'paperbnmmmnn'
y = 'titlesdfffdd'
dictt = {}
result = True

if len(x) != len(y):
    result = False
else:
    for i in range(len(x)):
        if x[i] not in dictt:
            dictt[x[i]] = y[i]
        else:
            if dictt[x[i]] != y[i]:
                result = False

# print(dictt)
print(result)

### Question 10
```
Imagine you took all the numbers between 0 and n and concatenated them together into a long string. How many digits are there between 0 and n? Write a function that can calculate this.
There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and 100.
Examples digits(1) ➞ 0
digits(10) ➞ 9
digits(100) ➞ 189
digits(2020) ➞ 6969
Notes The numbers are going to be rather big so creating that string won't be practical.
```

n = 2020

count = 0

for i in range(1, n):
    count += 1
    
    while i // 10 != 0:
        i = i // 10
        count += 1
print(count)

### Question 11
```
Print square pattern with alphabet symbols: 

input: pattern('A', 7)

output :
A A A A A A A 
B B B B B B B 
C C C C C C C 
D D D D D D D 
E E E E E E E 
F F F F F F F 
G G G G G G G 
```

import string

harf = string.ascii_uppercase

n = 9
s = 'X'
loc = harf.index(s)
res = ''

for i in range(n):
    res += ' '.join([harf[loc] for j in range(n)]) + '\n'
    loc += 1
    if loc > len(harf) - 1:
        loc = loc - len(harf)
res = res.rstrip('\n')
print(res)

### Question 12
```
Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.

Examples
tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]) ➞ "X"

tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
]) ➞ "O"

tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]) ➞ "Draw"
```

game = [
  ["X", "O", "O"],
  ["O", "X", "X"],
  ["X", "X", "X"]
]

result = 'Draw'
vertical = list(map(lambda *x : [*x], *game))

for i in range(len(game)):
    if len(set(game[i])) == 1 and game[i][0] != 'E':
        result = game[i][0]
        break
    elif len(set(vertical[i])) == 1 and vertical[i][0] != 'E':
        result = vertical[i][0]
        break
        
if result == 'Draw':
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 'E':
        result = game[0][0]
    elif game[0][2] == game[1][1] == game[2][0] and game[0][2] != 'E':
        result = game[0][2]

print(result)    

### Question 13
```
This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function
that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3},
{1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.
```

lst = [1, 2, 3, 4, 5]

arr = [[]]

for i in lst:
    for j in arr:
        arr = arr + [j + [i]]
        
print(arr)

### Question 14
```
This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10. Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
```

n = 200

number = 10
res = []

while True:
    summ = 0
    
    for i in str(number):
        summ += int(i)
        
    if summ == 10:
        res.append(number)
    number += 1
    
    if len(res) == n:
        result = res[-1]
        break
        
print(result)

### Question 15
```
An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

Incompatible types passed as n should return the string "Error".
```

# import numpy as np

# np.identity(5)

num = input('Enter an integer > ')

nums = num.lstrip('-')

lst = []
lst3 = []

if not nums.isdigit():
    print('Error')
else:
    if int(nums) == 0:
        print(lst)
    else:
        for i in range(int(nums)):
            lst2 = []
            for j in range(int(nums)):
                if i == j:
                    lst2.append(1)
                else:
                    lst2.append(0)
            lst3.append(lst2)
        
        if not num.startswith('-'):
            for i in lst3:
                print(i)
        else:
            for i in lst3:
                print(i[::-1])

### Question 16
```
This problem was asked by Yelp.
Given a mapping of digits to letters (as in a phone number), and a digit string,return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
```

dictt = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

number = 2356

str_num = str(number)

a = 0
b = 1

first = dictt[int(str_num[a])]
second = dictt[int(str_num[b])]

while True:
    res = []
    for i in first:
        for j in second:
            res.append(i+j)
    
    if b == len(str_num) - 1:
        break
    else:
        b += 1
        first = res
        second = dictt[int(str_num[b])]
print(res)

