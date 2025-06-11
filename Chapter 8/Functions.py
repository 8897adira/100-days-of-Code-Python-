#Argument passing
users = input("enter your name")
def Goodday(name, greet):
    print(greet + "good day!!!" + " " + name)
    return "good job"
a = Goodday(users, "How are you ???")
print(a)


#program to greet a user "good day"
user = input("enter your name")
def welcome():
    print(f"Good Day!!! {user}")


welcome()
    