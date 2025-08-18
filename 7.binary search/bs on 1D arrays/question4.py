#search insert position of target in array           #leetcode=35
def searchInsert(nums,n,target):
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=[3,4,6,7,9,12,16,17]
n=len(nums)
target=10
print(searchInsert(nums,n,target))