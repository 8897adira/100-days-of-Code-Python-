#write a program to find the factorial
P = int(input("enter your number: "))
product = 1
for i in range(1, P+1):
    product = product * i
print(f"the factorial of {P} is {product}!!")

#write a program to write the sum of all natural numbers
n = int(input("enter you number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum)
        
#write a program to know if the given number is prime
H = [2,5,6,8,7,3,23,19,61]

for i in H:
    if(i%2):
        print(f"{i} is prime number")
    
#Write a program to return only names starting with S
L = [ "Harry", "This",  "Falana", "Shubham", "Surabhi", "Sanvi"]

for name in L:
    if(name.startswith("S")):
        print(f"Hello {name}")

#write a program to write a table 
s = int(input("enter your number: "))

for i in range(1, 11):
    print(f"{s} X {i} = {s*i}")