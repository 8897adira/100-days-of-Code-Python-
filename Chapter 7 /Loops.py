
#while loop
d = 1

while(d<=3):
    print("Aditi")
    d +=1

# printing the values of the list using while loop

L = [1, "Harry", False, "This", 3, "Falana", "Shubham", 56]

i = 0

while(i<len(L)):
    print(L[i])
    i +=1
    
#For loop

for i in range(0,100,5):
    print(i)
 
 
# for loop with lists    
G = [1, "Harry", False, "This", 3, "Falana", "Shubham", 56]

i = 0

for i in G:
    print(i)
    
    
# for loop with string    
s = "hURRAY"

for i in s:
    print(i)
    
# for loop with else

h = [1, 56, 85, 96, 23, 100]

for i in h:
    print(i)
else:
    print("done")
    
#break, continue, pass(null statement that tells to do nothing)
for i in range(0,100,5):
    if (i==60):
        break #exit the loop right now
    elif (i == 40):
        continue #skips 40 
    print(i)
    




    
