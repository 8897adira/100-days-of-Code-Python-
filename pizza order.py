print("Welcome to python Pizza Deliveries!!")
size = input("What size of pizza do you want?? Small, Medium or Large : ")
pepperoni = input("Do you want pepperoni on your pizza ? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "Small":
   bill = 15
   
elif size == "Medium":
   bill = 20
   
elif size == "Large": 
   bill = 25

else:
    print("WRONG INPUTS!!!!")

if pepperoni == "Y":
    bill += 3    
else:
    print("no pepperoni added")

if extra_cheese == "Y":
    bill += 5
    print(f"your total amount for {size} pizza is ${bill}.")
else:
    print(f"your total amount for {size} pizza is ${bill}") 
  
    
    

     
    
    
