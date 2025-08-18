#impliment lower bound
#first index for with arr[i]>=target

def lb(nums,n,target):
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
target=3
print(lb(nums,n,target))