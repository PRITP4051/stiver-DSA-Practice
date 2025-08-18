#find square root of number
#brute force
# n=28
# ans=1
# for i in range(n):
#     if (i*i<=n):
#         ans=i
#     else:
#         break
# print(ans)


#optimal-binary search
def squareroot(n):
    low,high=1,n
    while low<=high:
        mid=(low+high)//2
        if (mid*mid<=n):
            low=mid+1
        else:
            high=mid-1
    return high
n=26
print(squareroot(n))

