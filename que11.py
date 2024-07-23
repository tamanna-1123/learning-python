# a program to display all prime numbers within a range(those which can not be multiplied by any number example 3,5,7,11)
start=25
end=50
print("prime number between",start, "and", end, "is")
for num in range (start,end+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0: #means if there is any factor
                break
        else:
             print(num)
                
        
    

