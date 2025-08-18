#count total number of occurence of x in sorted array

def first(nums,target):
            n=len(nums)
            low,high=0,n-1
            fir=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    fir=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return fir
def last(nums,target):
    n=len(nums)
    low,high=0,n-1
    las=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            las=mid
            low=mid+1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return las
def getfirstandlast(nums,target):
    f = first(nums,target)
    if f==-1:
         return [-1,-1]
    l = last(nums,target)
    return [f,l]
def count(nums,target) :
    f, l = getfirstandlast(nums,target)
    if f == -1:
        return 0
    return l - f + 1
nums=[5,7,7,8,8,10]
target=8
print(count(nums,target))
