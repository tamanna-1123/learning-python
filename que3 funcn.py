#return multiple values from a function
def calculation(a,b):
    addition=a+b
    subtraction=a-b
    multiplication=a*b
    return addition, subtraction, multiplication
result=calculation(10,50)
print(result)