talking=bool(input("enter a bool:"))
hour=float(input("enter a float:"))


def parrot_trouble(talking, hour):    
  
    return (talking and hour < 6 or hour > 21)

print(parrot_trouble(talking, hour))