#sort an array of 0's ,1's and 2's 
#ex arr=[2,0,2,1,1,0] ans=[0,0,1,1,2,2]
#brute force    merge sort

# def merge(arr, low, mid, high):               #leetcode=75
#     temp = []
#     left = low
#     right = mid + 1
#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1
#     while right <= high:
#         temp.append(arr[right])
#         right += 1
#     for i in range(low, high + 1):      #use to store all temp elements back to array
#         arr[i] = temp[i - low]

# def mergesort(arr, low, high):
#     if low >= high:
#         return
#     mid = (low + high) // 2
#     mergesort(arr, low, mid)
#     mergesort(arr, mid + 1, high)
#     merge(arr, low, mid, high)

# arr = list(map(int, input("Enter array elements (space-separated): ").split()))
# mergesort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)


#better
# cnt0,cnt1,cnt2=0,0,0
# arr=[0,1,1,0,1,2,1,2,0,0,0,1]
# n=len(arr)
# for i in range(n):
#     if arr[i]==0:
#         cnt0+=1
#     elif arr[i]==1:
#         cnt1+=1
#     else:
#         cnt2+=1
# for i in range(cnt0):
#     arr[i]=0
# for i in range(cnt0,cnt0+cnt1):
#     arr[i]=1
# for i in range(cnt0+cnt1,n):
#     arr[i]=2
# print(arr)

#optimal

a=[0,1,1,0,1,2,1,2,0,0,0,1]
n=len(a)
low,mid,high=0,0,n-1
while mid<=high:
    if a[mid]==0:
        a[low],a[mid]=a[mid],a[low]
        low+=1
        mid+=1
    elif a[mid]==1:
        mid+=1
    elif a[mid]==2:
        a[mid],a[high]=a[high],a[mid]
        high-=1
print(a)