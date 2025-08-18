# #minimum no of days to make m bouquets
# def possible(nums,day,m,k):
#     cnt=0
#     noofb=0
#     n=len(nums)
#     for i in range(n):
#         if nums[i]<=day:
#             cnt+=1
#         else:
#             noofb+=cnt//k
#             cnt=0
#     noofb+=cnt//k
#     return  noofb>=m
# def roseGarden(nums, k, m):
#     val = m * k
#     n = len(nums)  # size of the array
#     if val > n:
#         return -1  # impossible case
#     # find maximum and minimum
#     mini = float('inf')
#     maxi = float('-inf')
#     for i in range(n):
#         mini = min(mini, nums[i])
#         maxi = max(maxi, nums[i])

#     for i in range(mini, maxi+1):
#         if possible(nums, i, m, k):
#             return i
#     return -1

# nums = [7, 7, 7, 7, 13, 11, 12, 7]
# k = 3
# m = 2
# ans = roseGarden(nums, k, m)
# if ans == -1:
#     print("We cannot make m bouquets.")
# else:
#     print("We can make bouquets on day", ans)

    


#optimal
def possible(nums, day, m, k):
    n = len(nums)  # size of the array
    cnt = 0
    noOfB = 0
    # count the number of bouquets
    for i in range(n):
        if nums[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m

def roseGarden(nums, k, m):
    val = m * k
    n = len(nums)  # size of the array
    if val > n:
        return -1  # impossible case
    # find maximum and minimum
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, nums[i])
        maxi = max(maxi, nums[i])

    # apply binary search
    low = mini
    high = maxi
    while low <= high:
        mid = (low + high) // 2
        if possible(nums, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low
nums = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
ans = roseGarden(nums, k, m)
if ans == -1:
    print("We cannot make m bouquets.")
else:
    print("We can make bouquets on day", ans)


