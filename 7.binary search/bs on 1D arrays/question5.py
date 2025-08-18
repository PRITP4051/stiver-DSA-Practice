#floor and ceil in sorted array
# Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.

def findfloor(nums,n,target):
    low=0
    high=n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=target:
            ans=nums[mid]
            low=mid+1
        else:
            high=low-1
    return ans
def findceil(nums,n,target):
    low=0
    high=n-1
    floor,ceil=-1,-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=nums[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
def getFloorAndCeil(arr, n, x):
    f = findfloor(arr, n, x)
    c = findceil(arr, n, x)
    return (f, c)


arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = getFloorAndCeil(arr, n, x)
print("The floor and ceil are:", ans[0], ans[1])