#Reverse a given integer number
number=int(input("enter the number"))
reversed_number=0
print("given number",number)
while number>0:
    remainder=number%10
    reversed_number=(reversed_number*10)+remainder
    number=number//10
print("reversed number is",reversed_number)
    
    
