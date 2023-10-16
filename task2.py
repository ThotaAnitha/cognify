temp = float(input("enter Temperature:"))
unit = input("enter unit('c' for Celslus or 'f' for Fahrenheit):")
if unit == 'C' or unit=='c':
    newTemp = 9/5 * temp +32
    print("Temperature in celslus =",newTemp)
elif unit == 'F' or unit =='f' :
    newTemp = 5/9 *(temp - 32)
    print("Temperature in Fahrenheit =",newTemp)
else :
    print("unknown unit",unit)    
