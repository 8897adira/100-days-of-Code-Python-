'''
  *
 ***
*****
'''
n = 3        
for i in range(1, n+1): 
    print(" "*(n-i),end="") #2 spaces -> 
    print("*"*(2*i-1),end="") #1 star ->
    print("") #new line
    
    
'''
 ***
 ***
 ***
'''
m = 3 
for i in range(1, m+1):
    print(" "*(1),end="") #1 space in every loop ->
    print("*"*m,end="") #3 stars in every loop ->
    print("") #new line
    
'''
*
**
***
'''
o = 3
i = 0
for i in range(1, o+1): 
    print("*"*(i),end="") #1 star ->
    print("") #new line
    
'''
   *
  **
 ***
'''

p = 3
i = 0
for i in range(1, p+1):
    print(" "*(n-i),end="")
    print("*"*(i),end="")
    print("")
    
'''
*****
 ***
  *
'''

q = 3
i = 0
for i in range(q):
    print(" "*(i),end="") # starts with no space ->
    print("*"*(2*(q-i)-1),end="") # 5 stars ->
    print("") 

'''
 ***
 * *
 ***
'''

r = 3
for s in range(1, r+1):
    if (s==1 or s==r):
        print("*"* r, end="") # 3 stars
    else:
        print("*", end="") # 1 star
        print(" "*(r-2), end="") # 1 space
        print("*", end="")  # 1 star  
    print("") # new line
