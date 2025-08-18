# binary search to find x in sorted array          #leetcode=704

#iterative approch
# def bs(nums,n,target):
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             return mid
#         elif target>nums[mid]:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# nums=[3,4,6,7,9,12,16,17]
# n=len(nums)
# target=10
# print(bs(nums,n,target))

#recursive approch
def binarySearch(nums, low: int, high: int, target: int):
    if low > high:
        return -1  # Base case
    
    # Perform the steps:
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return binarySearch(nums, mid + 1, high, target)
    return binarySearch(nums, low, mid - 1, target)

def search(nums, target: int):
    return binarySearch(nums, 0, len(nums) - 1, target)

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = search(a, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind) 

