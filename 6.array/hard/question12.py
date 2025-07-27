#maximum product subarray   #leetcode=152
nums=[2,3,-2,4]
n = len(nums)
maxi = -10**5
prefix,sufix=1,1
product = 1
# Left to right pass
for i in range(n):
    if prefix==0:
        prefix=1
    if sufix==0:
        sufix=1
    prefix=prefix*nums[i]
    sufix=sufix*nums[n-i-1]
    maxi = max(maxi,max(prefix,sufix))
print(maxi)