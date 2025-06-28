#digit access
n=int(input("enter n:"))
count=0
while n!=0:
    rem=n%10
    count+=1
    n//=10
print(count)