

def IsPalindrome(num):
    
    if str(num) == str(num)[::-1]: #[::-1] = Reverses the string
        print("It is a palindrome!!")
    else:
        print("It is not a palindrome!!")


num = input("What is your word: ")


IsPalindrome(num)

