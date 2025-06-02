marks = {
    "Harry": 100,
    "Shubham" : 56,
    "Rohan": 25
}

print(marks)

print(marks["Harry"]) 

#methods of dictionary

print(marks.items()) #gives us a list
print(marks.keys()) #gives the items on the left side 
print(marks.values()) #gives the items on the right side 
marks.update({"Harry": 99}) #updates the value
print(marks)
print(marks.get("Harry")) #get method