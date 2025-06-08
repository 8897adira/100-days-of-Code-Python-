#take fruits from user and create a list with it
fruits = []
f1 = input("Enter fruits name:")
fruits.append(f1)
f2 = input("Enter fruits name:")
fruits.append(f2)
f3 = input("Enter fruits name:")
fruits.append(f3)
f4 = input("Enter fruits name:")
fruits.append(f4)
print(fruits)

#take the marks from user and display them in sorted manner
marks = []
m1 = input("Enter marks name:")
marks.append(m1)
m2 = input("Enter marks name:")
marks.append(m2)
m3 = input("Enter marks name:")
marks.append(m3)
m4 = input("Enter marks name:")
marks.append(m4)
marks.sort()
print(marks)

#print the sum of list
l1 = [2,3,5,60]
print(sum(l1))

#count the no, of zeros in tuple
tup = (7,0,8,0,0,9)
print(tup.count(0))