#search in rotated sorted array-2
def search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        #check if left part is sorted or not
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[low]<=nums[mid]:
            if nums[low]<=target and target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
        #check if right part is sorted or not
        if nums[mid]<=nums[high]:
            if nums[mid]<=target and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return False
nums=[4,5,6,7,0,0,1,2]
target=3
print(search(nums,target))

