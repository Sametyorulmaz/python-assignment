                              Question 1 

It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.

Create a function that takes the number of times a person washes their hands per day N and the number of months they follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands.

Examples

(8, 7) ➞ "588 minutes and 0 seconds"


(0, 0) ➞ "0 minutes and 0 seconds"


(7, 9) ➞ "661 minutes and 30 seconds"

Notes

Consider a month has 30 days.

Wash your hands.

per_day, months = list(map(int, input().split()))

total_seconds = 21 * per_day * 30 * months
minutes  = total_seconds // 60 
seconds = total_seconds % 60

print("{} minutes and {} seconds".format(minutes, seconds))

                              Question 2
Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in functions max() and sorted() are prohibited.

Examples

[3, 7, 2, 1, 7, 9, 10, 13] ➞ 10

[1, 3, 5, 7] ➞ -1

[0, 19, 18973623] ➞ 0

Notes

Consider using the modulo operator % or the bitwise and operator &.



arry = [3, 7, 2, 1, 7, 9, 10, 13]
max_even = -1

for i in arry :
  if i % 2 == 0 and i > max_even :
    max_even = i

print(max_even)

                              Question 3

Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".


For example, (121) should return "Evenish", since 1 + 2 + 1 = 4. (41) should return "Oddish", since 4 + 1 = 5.

Examples

(43) ➞ "Oddish"

4 + 3 = 7

7 % 2 = 1


(373) ➞ "Oddish"

3 + 7 + 3 = 13

13 % 2 = 1

(4433) ➞ "Evenish"

4 + 4 + 3 + 3 = 14

14 % 2 = 0

num = input("")
total = 0

for i in num :
  total += int(i)

if total % 2 : 
  print("Oddish")
else :
  print("Evenish")

# print("Evenish" if total % 2 == 0 else "Oddish" )

                              Question 4

Program to print pyramid a using numbers.(User enter the numbers of rows)




# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = int(input(""))

for i in range(1, rows+1) :
  print(i * (str(i)+ " "))


rows = int(input(""))

for i in range(1, rows+1) :
  print(* (i * str(i)))

                              Question 5
Fruit salads are served best when the fruits are sliced and diced into small chunks!

For this challenge, slice each fruit in half and sort the chunks alphabetically. This recipe tastes best when the chunks are joined together to make a string.

Worked Example

["apple", "pear", "grapes"] ➞ "apargrapepesple"

Chunks: ["ap", "ple", "pe", "ar", "gra", "pes"]

Sorted chunks: ["ap", "ar", "gra", "pe", "pes", "ple"]

Final string: "apargrapepesple"

Examples

["apple", "pear", "grapes"] ➞ "apargrapepesple"

["raspberries", "mango"] ➞ "erriesmangoraspb"

["banana"] ➞ "anaban"

Notes

If a fruit has an odd number of letters, make the right side larger than the left.

For example: "apple" will be sliced into "ap" and "ple".

All fruits will be given in lowercase.


arry = ["apple", "pear", "grapes"]
new_arry = []
for i in arry :
  new_arry += [i[: len(i)//2]]
  new_arry += [i[len(i)//2 :]]

salad = "".join(sorted(new_arry))
salad


                                Question 6
Given a positive integer N, The task is to write a Python program to check if the number is prime or not.

Definition:

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

The first few prime numbers are {2, 3, 5, 7, 11, ….}.

number = int(input("Please enter a number : "))

for i in range(2,number) :
  if number % i == 0 :
    print(False)
    break
else :
  print(True)

number = int(input("Please enter a number : "))
division = []
for i in range(1,number+1) :
  if number % i == 0 :
    division += [i]
print("False" if len(division) > 2 else "True")


                                Question 7
Create a function that takes a word and extends all vowels by a number num.

Examples


"Hello", 5 ➞ "Heeeeeelloooooo"

"Edabit", 3 ➞ "EEEEdaaaabiiiit"

"Extend", 0 ➞ "Extend"


word = input("Please enter a word : ")
num = int(input(""))
vowels ="aeiouAEIOU"
new_w = ""

for i in word :
  if i in vowels and num > 0 :
    new_w += i * (num + 1)
  elif i in vowels and num == 0 :
    new_w += i 
  else :
    new_w += i 

print(new_w)



