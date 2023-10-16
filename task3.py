import re
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return True
    return Flase
email =str(input("ENTER YOUR EMAIL ADDRESS::"))
if validate_email(email):
    print("valid email address")
else:
    print("invalid email address") 
       