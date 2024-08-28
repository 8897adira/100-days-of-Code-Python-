import random


#generating a random number between 1 to 10
random_integer = random.randint(1,10)
print(random_integer)

#generating a random float number
random_number_0_to_1 = random.random() 
print(random_number_0_to_1)

#generating a random float number from a given range
random_float = random.uniform(1,10)
print(random_float)

#generating a heads or tails randomly
random_th = random.randint(1,2)
if random_th == 1:
    print("Heads")
else:
    print("Tails")

#Lists
fruits = ["Apple","Orange","Pineapple"]
print(fruits[2])

#Who will pay the bill

friends = ["Alice","Bob","Charlie","David","Emanuel"]
print(random.choice(friends))

#length of the list

num_of_fruits = len(fruits)
print(num_of_fruits)

#nested list

fam = [fruits , friends]
print(fam)
print(fam[1][1])
