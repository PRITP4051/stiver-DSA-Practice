# wap whether the given number is prime or not
n=int(input("enter the number:"))
if n>0:
    for i in range(2,n):
        if(n%i!=0):
            print(n,"is the prime number.")
        else:
            print(n,"is not the prime number")
else:
    print(n,"is not the prime number.")