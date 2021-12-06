num1=int(input("enter a number:"))
num2=int(input("enter a number:"))

def sum_double(x, y):
  
    if x == y :
          
        print((x + y)*2)
    
    else:
        
        print(x + y)

        sum_double(num1,num2)