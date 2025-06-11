        
#write a program to convert inches to cms
inches = int(input("enter the inches:  "))

def cms():
    return (inches * 2.54)
        
print(f" the answer will be {cms()}cm")




#write a recursive function to calculate the sum of first n natural numbers
n = int(input("enter the number to find the sum of natural numbers: "))

def nnum(n):
    if (n == 1):
        return 1
    return (n + nnum(n-1))

print(f"the sum of first {n} natural numbers is: {nnum(n)} ")


#write a program using functions to find greatest of three numbers
n = int(input("enter your number"))
m = int(input("enter your number"))
o = int(input("enter your number"))

def biggestnum():
    if (n > m > o):
      return n
    elif (m > n > o ):
        return m
    else:
        return o

print(f"the greatest number is: {biggestnum()}")

#write a program using function to convert celcius to Fahrenheit

temperature = int(input("enter the temperature in celcius:  "))

def temp():
    return (temperature * 9/5) + 32
        
print(f" the answer will be {temp()}°F")
     