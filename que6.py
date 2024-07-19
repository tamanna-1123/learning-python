n=int(input("enter the number"))
count=0
while n>0:
    n=n//10
#we used //(floor division)means we will get answr in integer,and it is used here because when ever we divide any number from 10 we 
# will get 1- from that number for example if we have 234 and we divide that by 10 we'll get 23 as 4 will not show that's how loop
# will work
    count=count+1
print("total count:",count)