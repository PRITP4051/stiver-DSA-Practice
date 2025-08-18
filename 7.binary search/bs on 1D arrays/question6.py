#first and last occurence of a number in array          #leetcode=34
#linear search 
#brute force

# nums=[5,7,7,8,8,10]
# n=len(nums)
# target=8
# first,last=-1,-1
# for i in range(n):
#     if nums[i]==target:
#         if first==-1:
#             first=i
#         last=i
# print([first,last])

#optimal
#binary search
#lower and upper bound
# def lb(nums,n,target):
#     low=0
#     high=n-1
#     ans=n
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]>=target:
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ans
# def ub(nums,n,target):
#     low=0
#     high=n-1
#     ans=n
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]>target:
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ans
# def search(nums,n,target):
#     lowerb=lb(nums,n,target)
#     if lowerb==n or nums[lowerb]!=target:
#         return [-1,-1]
#     return [lowerb,ub(nums,n,target)-1]
# nums=[5,7,7,8,8,10]
# print(search(nums,len(nums),8))


#first and last uses
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
nums=[5,7,7,8,8,10]
target=8
print(getfirstandlast(nums,target))
