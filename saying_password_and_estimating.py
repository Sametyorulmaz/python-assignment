
#*****Saying Password
name = "Sam"
password = "xwz,0947"
user = input("Enter your name :").title()
if user == name :
    print(f"Hello, {name} !The password is : {password}")
else :
    print(f"Hello, {user} !See you later.")
    

#*****Estimating the risk of death from coronavirus.
#*****Takes "Yes" or "No" from the user as an answer to the following questions :

age = input("Are you a cigarette addict older than 75 years old?: Yes or No >> ").title()
chronic = input("Do you have a severe chronic disease?: Yes or No >> ").title()
immune = input("Is your immune system too weak?: Yes or No >> ").title()


if age == "Yes" or chronic == "Yes" or immune == "Yes":
  print("You are in risky group")
else:
  print("You are not in risky group")  