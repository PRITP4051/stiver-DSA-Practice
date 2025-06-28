#wap to print name n times using recursion
i=1
def name(i,n):
    if i>n:         #base case
        return
    print("PRIT")
    name(i+1,n)
n=int(input("enter n: "))
name(1,n)

