#fibonacci number
# def fin(n):                            #leetcode=509
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return fin(n-1)+fin(n-2)
# n=int(input("enter nth term: "))
# print(fin(n))

# def fin(n):
#     if n<=1:
#         return n
#     return fin(n-1)+fin(n-2)
# n=int(input("enter nth term: "))
# print(fin(n))

def fin(n):
    if n<=1:
        return n
    last=fin(n-1)
    slast=fin(n-2)
    return last+slast
n=int(input("enter nth term: "))
print(fin(n))
    