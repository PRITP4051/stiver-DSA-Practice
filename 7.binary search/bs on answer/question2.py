#Nth root of any number
# Input: N = 3, M = 27
# Output: 3
# Explanation: The cube root of 27 is equal to 3.
# Input: N = 4, M = 69
# Output:-1
# Explanation: The 4th root of 69 does not exist. So, the answer is -1.

#brute force
# def nthroot(n,m):
#     for i in range(m):
#         if i**n==m:
#             return i
#     return -1
# print(nthroot(3,27))

#optimal
#binary search
# def nthroot(n,m):
#     low,high=1,m
#     while low<=high:
#         mid=(low+high)//2
#         if mid**n==m:
#             return mid
#         else:
#             high=mid-1
#     return -1
# print(nthroot(4,16))



#give function to find mid^n 

def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)

