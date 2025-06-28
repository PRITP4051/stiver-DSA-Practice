#print n to 1 using backtracking(not use -=) and recursion
def print_i(i,n):
    if i>n:
        return
    print_i(i+1,n)
    print(i)
n=int(input("enter n:"))
print_i(1,n)