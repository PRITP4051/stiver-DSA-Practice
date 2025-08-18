#find minimum in rotated sorted array
import sys
def minimum(nums):
    mini=sys.maxsize
    n=len(nums)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if nums[low] <= nums[high]:
            mini = min(mini, nums[low])
            break
        if nums[low] <= nums[mid]:
            mini=min(mini,nums[low])
            low=mid+1
        else:
            mini=min(mini,nums[mid])
            high=mid-1
    return mini
nums=[4,0,1,2,3]
print(minimum(nums))