#print 1 to n using recursion
count=1
def print_count(count,n):
    if count>n:
        return
    print(count)
    print_count(count+1,n)
n=int(input("enter n: "))
print_count(1,n)


    