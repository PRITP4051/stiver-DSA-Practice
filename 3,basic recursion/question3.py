#print n to 1 using recursion
# def print_n(n,count=1):
#     if n<count:
#         return
#     print(n)
#     print_n(n-1,count)
# n=int(input("enter n: "))
# print_n(n)


#method 2
# def print_n(n):
#     if n==0:
#         return
#     print(n)
#     print_n(n-1)
# n=int(input("enter n: "))
# print_n(n)

#method 3
count=1
def print_count(count,n):            #main method simple change count+1 to -1
    if count<1:
        return
    print(count)
    print_count(count-1,n)
n=int(input("enter n: "))
print_count(n,n)
