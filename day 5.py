#for loop

fruits = ["Apple", "Orange" , "Pineapple"]
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")

#Highest score 
student_scores = [150, 142, 185, 173, 189, 169, 146]
highest_score = max(student_scores)
print(highest_score)

#sum of score
sumofscore = sum(student_scores)
print(sumofscore)

#method 2 of higgest score
max_score = 0
for score in student_scores:
    if score > max_score:   #150 > 0, 142>150, 185>150
        max_score = score   #max_score = 150 then 150 then 185 
print(max_score)

#adding numbers using range()

num = 0
for number in range(1, 101):
    num += number
print(num)


#You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
#Your program should print each number from 1 to 100 in turn and include number 100.
#But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
for number in range(1 , 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
  
