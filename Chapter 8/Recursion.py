#Recursion is a function that calls itself
 
#finding the factorial of a number
 
 
n = int(input("enter your number: "))
def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

print(f"the factorial for {n} is : {factorial(n)}")

