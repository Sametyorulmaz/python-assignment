<h1><center>Python Workshop - 03.12.2021</center></h1>

### Question 1
```
# https://edabit.com/challenge/646cCaFig6AP89YRo

With List Comprehension Solution:

Write a program that returns a list of all the numbers from 1 to an integer argument. But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.

fizz_buzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

fizz_buzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"] 
```



### Question 2
```
https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma

An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False

Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.
```



### Question 3
```
https://edabit.com/challenge/fmQ9QvPBWL7N9hSkq

Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.

unstretch("ppoeemm") ➞ "poem"

unstretch("wiiiinnnnd") ➞ "wind"

unstretch("ttiiitllleeee") ➞ "title"

unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"

Final strings won't include words with double letters (e.g. "passing", "lottery").
```



### Question 4
```
https://edabit.com/challenge/6CGomPbu3dK536PH2

Create a function that takes in a list and returns a list of the accumulating sum.

accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]
# [1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]

accumulating_list([1, 5, 7]) ➞ [1, 6, 13]

accumulating_list([1, 0, 1, 0, 1]) ➞ [1, 1, 2, 2, 3]

accumulating_list([]) ➞ []

An empty list input [] should return an empty list [].
```



### Question 5
```
# Write a Python code to sort the list at below without using .sort() method of list. elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11] Expected output: [2, 11, 12, 45, 77, 99, 333, 999, 8982]
```



### Question 6
```
https://edabit.com/challenge/6vSZmN66xhMRDX8YT

Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

Notes
The sublists should be returned in the order of each element's first appearance in the given list.
```



### Question 7
```
https://edabit.com/challenge/YN33GEpLQqa5imcFx

The goal of this challenge is to return Pascal's triangle up to number 29. Pascal's triangle is the sum of the two upper corners.
    1
   1 1
  1 2 1
 1 3 3 1

# There will always be the 1 in the first
# place and the row in the second.

Create a function that returns a row from Pascal's triangle. To find the row and column you can use n!/(k!*(n-k)!) where n is the row down and k is the column.

pascals_triangle(1) ➞ "1 1"

pascals_triangle(4) ➞ "1 4 6 4 1"

pascals_triangle(6) ➞ "1 6 15 20 15 6 1"

pascals_triangle(8) ➞ "1 8 28 56 70 56 28 8 1"
```

