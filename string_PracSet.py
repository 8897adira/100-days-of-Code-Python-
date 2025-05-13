name = input("enter your name: ")
print(name + ", Good Afternoon")
print(f"Good Afternoon, {name}")
date = "3 nov"
letter =  (f"Dear {name}, \n You are Selected \n {date}")
print(letter)

# eliminating double space in a string
names = "Aditi is a good  girl  "
print(names.find("  ")) #returns the index if not then returns -1

# replacing double space in a string
names = "Aditi is a good  girl  "
print(names.replace("  "," "))

#Write a proram to format the following letter using escape sequance characters 
letters = "Dear Harry, \n\tThis python course is nice. \n\"Thanks\"!!"
print(letters)