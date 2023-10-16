def palindrome(s):
    if s == s[::-1]:
        return("string is a palindrome")
    else:
        return("string is not palindrome")
s=str(input("ENTER ANY STRING::"))
print(palindrome(s))    
