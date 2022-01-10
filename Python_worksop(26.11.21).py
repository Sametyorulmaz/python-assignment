                                  Exercise-1

Convert a Number to Base-2
Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

Examples

binary(1) ➞ "1"

// 1 * 1 = 1

binary(5) ➞ "101"

// 1 * 1 + 1 * 4 = 5

binary(10) ➞ "1010"

// 1 * 2 + 1 * 8 = 10

Note (Don't use bin() function)

def binary(num) :
  bin = ""
  while num != 0 :
    bin += str(num % 2)
    num = num // 2
  return  bin[::-1]

binary(10)


                                  Exercise-2 
Check if One Array can be Nested in Another

Create a function that returns true if the first array can be nested inside the second.

arr1 can be nested inside arr2 if:

arr1's min is greater than arr2's min.

arr1's max is less than arr2's max.

Examples

canNest([1, 2, 3, 4], [0, 6]) ➞ True

canNest([3, 1], [4, 0]) ➞ True

canNest([9, 9, 8], [8, 9]) ➞ False

canNest([1, 2, 3, 4], [2, 3]) ➞ False

def canNest(arry1, arry2) :
  return min(arry1) > min(arry2) and max(arry1) < max(arry2)

canNest([1, 2, 3, 4], [2, 3])

                                    Exercise-3
Move Capital Letters to the Front

Create a function that moves all capital letters to the front of a word.

Examples

cap_to_front("hApPy") ➞ "APhpy"

cap_to_front("moveMENT") ➞ "MENTmove"

cap_to_front("shOrtCAKE") ➞ "OCAKEshrt"

def cap_to_front(text):
  new_text = ""
  for i in text :
    if i.isupper() :
      new_text += i
      text = text.replace(i,"")
  return new_text + text

cap_to_front("hApPy")

def cap_to_front(text):
 return "".join([i for i in text if i.isupper()]+ [i for i in text if i.islower()])

cap_to_front("hApPy")

                                  Exercise-4
The Reverser!

The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples

reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"

Notes

There will be no punctuation in any of the test cases.

def reverse(text) :
  return "".join([i.lower() if i.isupper() else i.upper() for i in text[::-1]])

reverse("Radar")

                                    Exercise-5
Create a function that retrieves every number that is strictly larger than every number that follows it.
Examples

[3, 13, 11, 2, 1, 9, 5] ➞ [13, 11, 9, 5]

13 is larger than all numbers to its right, etc.

[5, 5, 5, 5, 5, 5] ➞ [5]

Must be strictly larger.

Always include the last number.

[5, 9, 8, 7] ➞ [9, 8, 7]

Notes

The last number in an array is trivially strictly larger than all numbers that follow it (no numbers follow it).

arry = [5, 5, 5, 5, 5, 5]
n_arry = []
for i in  range(0,len(arry)-1) :
  if all([arry[i] > j for j in arry[i+1:]]) == True :
    n_arry += [arry[i]]
n_arry + [arry[-1]]

                                    Exercise - 6
C * ns * r * d Str * ngs

Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

Example

uncensor("Wh * r * d * d my v * w * ls g * ?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("* PP * RC * S * ", "UEAE") ➞ "UPPERCASE"

Notes

The vowels are given in the correct order.

The number of vowels will match the number of * characters in the censored string.

def uncensor(string, vowel) :
  count = 0
  n_str = ""
  for i in string :
    if i == "*" :
      n_str += vowel[count]
      count += 1
    else :
      n_str += i
  return n_str

uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")

                                    Exercise -7
There is a string, s , of lowercase English letters that is repeated infinitely many times. Given an integer, n , find and print the number of letter a's in the first n letters of the infinite string.

Example
s = "abcac"

n = 10

The substring we consider is "abcacabcac", the first 10 characters of the infinite string. There are 4  occurrences of a in the substring.

def repeatedString(s, n):
  return (s * (n // len(s)) + s[0:(n % len(s))]).count("a")

repeatedString("abcabc" ,125 )

def repeatedString(s, n):
    c = s.count('a')
    div=n//len(s)
    if n%len(s)==0:
        c= c*div
    else:
        m = n%len(s)
        c= c*div+s[:m].count('a')
    return c

                                Exercise -8
Nearest Vowel

Given a letter, created a function which returns the nearest vowel to the letter. If two vowels are equidistant to the given letter, return the earlier vowel.

Examples

nearestVowel("b") ➞ "a"

nearestVowel("s") ➞ "u"

nearestVowel("c") ➞ "a"

nearestVowel("i") ➞ "i"

Notes

All letters will be given in lowercase.

There will be no alphabet wrapping involved, meaning the closest vowel to "z" should return "u", not "a".

vowel = "aeiou"
string = "t"
order = []
for i in vowel :
  order += [abs(ord(i) - ord(string))]

vowel[order.index(min(order))]


def nearestVowel(string) :
  vowel = "aeiou"
  order = [abs(ord(i) - ord(string)) for i in vowel]
  return vowel[order.index(min(order))]

nearestVowel("z")

