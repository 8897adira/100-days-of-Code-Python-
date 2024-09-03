#Password Generator
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*']

print("Welcome to Password Generator")

passwrd = int(input("How many letters do you need your password to be? : "))
sym = int(input("How many symbols do you need in your password? : "))
num = int(input("How many numbers do you need in your password? : "))

#1st Solution

password = ""

for char in range(1 , passwrd + 1):
    password += random.choice(letters)
for numb in range(1 , num + 1):
    password += random.choice(numbers)
for symb in range(1 , sym + 1):
    password += random.choice(symbols)

print(f"Your Password is : {password}")

#2nd Solution

password_2 = ""

for char in range(1 , passwrd + 1):
    password_2 += random.choice(letters)
for numb in range(1 , num + 1):
    password_2 += random.choice(numbers)
for symb in range(1 , sym + 1):
    password_2 += random.choice(symbols)

final_pass = ''.join(random.sample(password_2, len(password_2))) #Jumbles the characters in the password_2
print(f"Your Password is : {final_pass}")


 


