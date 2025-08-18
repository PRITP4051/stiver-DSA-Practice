# #find the smallest divisor with given threshold 
# #same as koko eating bananas
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
import math
def maximum(nums):
    n=len(nums)
    maxi=float('-inf')
    for i in range(n):
        maxi=max(maxi,nums[i])
    return maxi
def calculateTotaldivison(nums,divide):
    totald= 0
    n = len(nums)
    # Find total hours
    for i in range(n):
        totald += math.ceil(nums[i] / divide)
    return totald

def smallestdivisor(nums, threshold):
    low = 1
    high = maximum(nums)
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        totald = calculateTotaldivison(nums, mid)
        if totald <= threshold:
            high = mid - 1
        else:
            low = mid + 1
    return low
nums=[1,2,5,9]
threshold=6
print(smallestdivisor(nums,threshold))