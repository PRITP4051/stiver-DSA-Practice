#print 1 to n using backtracking (no use of +=) and recursion
def print_i(i,n):
    if i<1:
        return
    print_i(i-1,n)
    print(i)
n=int(input("enter n: "))
print_i(n,n)