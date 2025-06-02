#write a program to check if a given number is present in the list or not

a = [ 1, 2, 5, 6.5, 8, 23, 3]
num = float(input("enter you number: "))

if (num in a):
    print("your number is present!!")
else:
    print("no match found!!!")




# write a program to check if the username contains 10 characters or not.

username = input("Enter Username: ")
if ((len(username)) > 10):
    print("the username is tooo lengthy")
else:
    print("You are good to go!!")




a = int(input("Enter your Age: "))

# if elif else ladder

if(a>=18):
    print("Yes")
elif(a<0):
    print("Are you drunk???????")
else:
    print("You are baccha!!!!!!")
    
#print the greatest number 

a1 = int(input("enter number 1: "))
a2 = int(input("enter number 2: "))
a3 = int(input("enter number 3: "))

if (a1> a2 and a1> a3 ):
    print("the greatest is " , a1)
elif (a2>a1 and a2 > a3):
    print("the greatest is " , a2)
else:
    print("the greatest is " , a3)
    
    

