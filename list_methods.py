friends = ["apple", "Orange", 5, 3.14, False, "Prachi"]
print(friends)
friends.remove("Orange")
friends.append("Aditi") #adds an item to the end of the list
friends.insert(3, "Parth") #inserts the item in the list (index , item)
print(friends)

l1 = [5,6,8,1,9,4,3,2,7,6,8]
v = l1.count(6) #counts the no. of times an item is present in the list
print(v)
value = l1.pop(4)#removes the item (index)
print(value)
l1.sort()#sorts the list in increasing order
l1.reverse() #reverses the list
print(l1)


