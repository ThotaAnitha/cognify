print("_________BASIC CALCULATION_________")
x=float(input("ENTER ANY NUMBER"))
y=float(input("ENTER ANY NUMBER"))
print("type of operation to be perfromed on the given numbers=>>")
print(" 1)Addition ")
print(" 2)Subtraction ")
print(" 3)Division")
print(" 4)Multipication")
print(" 5)Reminder")
print(" 6)FloorDiv")
operation=input("which operation do you want to perform==>>")
if operation=='Addition' or operation=='+' or operation=='Add' or operation=='1':
   print("Addition of given numbers is==>",(x+y))
elif operation=='Subtraction' or operation=='-' or operation=='Sub' or operation=='2':
     print("Subtraction of given numbers is =>",(x-y))    
elif operation=='Multipication' or operation=='*' or operation=='Mul' or operation=='4':
     print("ultipication of given numbers is =>",(x*y))  
elif operation=='Division' or operation=='/' or operation=='Div' or operation=='3':
     print("Division of given numbers is =>",(x/y))  
elif operation=='Reminder' or operation=='%' or operation=='Rem' or operation=='5':
     print("Reminder of given numbers is =>",(x%y))    
elif operation=='FloorDiv' or operation=='//' or operation=='FD' or operation=='6':
     print("FloorDiv of given numbers is =>",(x//y))                