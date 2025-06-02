p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("enter your message to be checked: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Alert !!!! this is a spam message!!!!!")
else:
    print("this is safe!!!!!!")