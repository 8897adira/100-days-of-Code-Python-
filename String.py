name = "Aditi" #sequence of characters is a string

#length of string
namelen = len(name)
print(namelen)

#slicing of string
sl = name[0:3]
print(sl)

#skiping values
num = "1234567890"
skp = num[0:5:2]
print(skp) #135

#Functions

print(name.endswith("ti")) #gives a boolean value whether true or false
print(name.startswith("ad")) #it is case sensitive
print(name.capitalize()) #converts the first char into caps
print(name.upper()) #converts the whole word into caps
print(name.count("i")) #counts how many times a character occurs in the word

#Escape sequence

a = "Aditi is a good girl\nbut \"not\" that\'s good"
print(a) 


