                #Python Basic & Plus Workshop -4

# Subject: Collections - Control Flow Statements - Functions

## Coding Challenge -1 : Palindrome

Purpose of the this coding challenge is to solve a control flow statements issue.

### Learning Outcomes

At the end of the this coding challenge, students will be able to;

- understand the use of loops.
- understand the importance of alphanumeric string methods.
- get a better understanding in manipulating strings.

### Problem Statement
  
- Write a function/functions that checks whether the sentence you get from the user is a **palindrome**. (Do not consider punctuation and special characters. Only consider "***alphanumeric***" characters.)


```bash
input : "ey edip adana'da, pide ye!"

output : "ey edip adana'da, pide ye!" is a palindrome

input : "Was it a car or a cat I saw?"

output : "Was it a car or a cat I saw?" is a palindrome
```

### Solution :

def palindrome(cumle):
    result = [i.lower() for i in cumle if i.isalnum() ]
    if result == result[::-1]:
      return f"{cumle} is palindrome."
    else:
      return f"{cumle} is not a palindrome."


palindrome("ey edip adana'da, pide ye!")

def palindrome(cumle):
    result = ""
    for i in cumle:
      if i.isalnum():
        result += i
    if result == result[::-1]:
      return f"{cumle} is palindrome."
    else:
      return f"{cumle} is not a palindrome."

palindrome("ey edip adana'da, pide ye!")

## Coding Challenge - 2: Sudoku Format Converter&Printer

The purpose of this coding challenge is to write a program that prints the given lists as sudoku looking format.

### Learning Outcomes

At the end of this coding challenge, students will be able to;

- analyze a problem, identify, and apply programming knowledge for appropriate solution.

- design, implement `arithmetic operators` and nested loops effectively in Python to solve the given problem.

- demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

### Problem Statement

<div class="alert alert-block alert-info">
    <b>💡Objective:</b>
    <ul>
        <li>To improve your <b>control flow statement</b> skills.</li>
    </ul>
</div>

<hr>
<p><b>Task:</b> The department you work for has received a project that displays the solved sudoku puzzles in a digital environment.&nbsp;</p>
<p></p>
<p></p>
<ul>
    <li>Write a Python code to print out the given <code>sudoku</code> puzzle matrix in the following format.</li>
</ul>
<b>Given format :</b><br>
<ol>
</ol>
<p>
</p>
<div>
    <pre>sudoku&nbsp;=&nbsp;[<br>&nbsp;&nbsp;&nbsp;&nbsp;[0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;6,&nbsp;4,&nbsp;0,&nbsp;0,&nbsp;0],<br>&nbsp;&nbsp;&nbsp;&nbsp;[7,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;3,&nbsp;9,&nbsp;0],<br>&nbsp;&nbsp;&nbsp;&nbsp;[8,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0],<br>&nbsp;&nbsp;&nbsp;&nbsp;[0,&nbsp;0,&nbsp;0,&nbsp;5,&nbsp;0,&nbsp;2,&nbsp;0,&nbsp;6,&nbsp;0],<br>&nbsp;&nbsp;&nbsp;&nbsp;[0,&nbsp;8,&nbsp;0,&nbsp;4,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0],<br>&nbsp;&nbsp;&nbsp;&nbsp;[3,&nbsp;5,&nbsp;0,&nbsp;6,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;7,&nbsp;0],<br>&nbsp;&nbsp;&nbsp;&nbsp;[0,&nbsp;0,&nbsp;2,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;3],<br>&nbsp;&nbsp;&nbsp;&nbsp;[0,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;5,&nbsp;9,&nbsp;0,&nbsp;0,&nbsp;0],<br>&nbsp;&nbsp;&nbsp;&nbsp;[0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;7,&nbsp;0,&nbsp;0]<br>]</pre>
    <div>
        <b>Desired output format :</b><br>
        <ol>
        </ol>
    </div>
    <pre>- - - - - - - - - - - - - - - 
0  0  0  | 0  6  4  | 0  0  0  
7  0  0  | 0  0  0  | 3  9  0  
8  0  0  | 0  0  0  | 0  0  0  
- - - - - - - - - - - - - - - 
0  0  0  | 5  0  2  | 0  6  0  
0  8  0  | 4  0  0  | 0  0  0  
3  5  0  | 6  0  0  | 0  7  0  
- - - - - - - - - - - - - - - 
0  0  2  | 0  0  0  | 1  0  3  
0  0  1  | 0  5  9  | 0  0  0  
0  0  0  | 0  0  0  | 7  0  0  
- - - - - - - - - - - - - - -</pre>
</div><br>
<p></p>
<p></p>
<hr>
<p><i><b>Note that</b>; <br></i></p>
<ul>
    <li><i><i>Use not more than "<b>control flow statement and boolean logic operators</b>" in solving this code problem. </i></i>
    </li>
    <li><i><i>The output which we expect from you is only a new output format above. </i></i>
    </li>
    <li><i><i>We don't expect a sudoku puzzle solver from you.</i></i>
    </li>
</ul>
<p></p>

### Solution :

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

c1 = 0
for i in sudoku:
  print()
  if c1 % 3 == 0:
    print("- - - - - - - - - - - - - - - ")
  c2 = 0  
  c1 += 1  
  for j in i:
    if c2 != 0 and c2 % 3 == 0:
      print("| ", end = "")
    c2 += 1  
    print(j, " ", end = "")
  if c1 == len(sudoku):
    print("\n"+"- - - - - - - - - - - - - - - ")
