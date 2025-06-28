#gretest comman division
# n1=int(input("enter first number:"))
# n2=int(input("enter second number:"))
# gcd=1
# for i in range(1,min(n1,n2)+1):
#     if(n1%i==0 and n2%i==0):
#         gcd=i
#         print(gcd)

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
while(n1>0 and n2>0):
    if n1>n2:
        n1=n1%n2
    else:
        n2=n2%n1
if (n1==0):
    print(n2)
else:
    print(n1)