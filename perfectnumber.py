n=int(input("enter a number:\n"))
temp=n
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==temp):
    print("perfect")
else:
    print("not")
