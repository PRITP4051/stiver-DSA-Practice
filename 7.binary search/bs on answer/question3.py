#koko eating bananas
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

#optimal my trick
# def ans(nums,h,mid):
#     ans=0
#     for i in nums:
#         if i%mid==0:
#             i=i//mid
#         else:
#             i=(i//mid)+1
#         ans=ans+i
#         if ans>h:
#             return 1
#     if ans<=h:
#         return 0
# def koko(nums,h):
#     low=1
#     high=max(nums)
#     k=0
#     while low<=high:
#         mid=(low+high)//2
#         midn=ans(nums,h,mid)
#         if midn==0:
#             k=mid
#             high=mid-1
#         elif midn==1:
#             low=mid+1
#     return k
# nums=[30,11,23,4,20]
# h=6
# print(koko(nums,h))   

#siver trcik
import math

def findMax(v):
    maxi = float('-inf')
    n = len(v)
    # Find the maximum
    for i in range(n):
        maxi = max(maxi, v[i])
    return maxi

def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def minimumRateToEatBananas(v, h):
    low = 1
    high = findMax(v)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        totalH = calculateTotalHours(v, mid)
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

v = [30,11,23,4,20]
h = 5
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")
