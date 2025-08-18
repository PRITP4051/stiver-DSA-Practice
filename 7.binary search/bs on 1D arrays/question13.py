#peak element in array
#a[i]>a[i-1] and a[i]>a[i+1]

def peak(nums):
    n=len(nums)
    if n==1:
        return 0
    if nums[0]>nums[1]:
        return 0
    if nums[n-1]>nums[n-2]:
        return n-1
    low,high=1,n-2
    while low<=high:
        mid=(low+high)//2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
    # If we are in the left:
        if nums[mid] > nums[mid - 1]:
            low = mid + 1
    # If we are in the right:
    # Or, arr[mid] is a common point:
        else:
            high = mid - 1
    return -1
nums=[1,2,3,4,5,6,7,8,5,1]
print(peak(nums))