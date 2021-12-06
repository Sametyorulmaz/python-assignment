num=int(input("enter a number:"))

def fizz_buzz(num):
    
    return["FizzBuzz" if not  n %15 else 
           "Buzz" if not n % 5 else
           "Fizz" if not n % 3 else 
           n for n in range(1, num+1)]

print(fizz_buzz(num))