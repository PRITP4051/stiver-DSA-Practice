#right rotate array d times             #leetcode=189
#brute force

# arr = list(map(int, input("enter array element(saperated by space): ").split()))
# n = len(arr)
# d = int(input("Enter k (number of rotations): "))
# d = d % n  # To handle cases where k > n
# temp=[]
# for i in range(n-d,n):
#     temp.append(arr[i])
# for i in range(n-1,d-1,-1):
#     arr[i] = arr[i - d]
# for i in range(0,d):
#     arr[i]=temp[i]
# print(arr)

#optimal approch
def reverse_subarray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = list(map(int, input("enter array element(saperated by space): ").split()))
n = len(arr)
d = int(input("Enter k (number of rotations): "))
d = d % n  # To handle cases where k > n

reverse_subarray(arr, 0, d)
reverse_subarray(arr,d+1,n-1)
reverse_subarray(arr, 0, n - 1)
print(arr)


#thinking solution
# arr = list(map(int, input("enter array element(saperated by space): ").split()))
# n = len(arr)
# d = int(input("Enter k (number of rotations): "))
# d = d % n  # To handle cases where k > n
# arr=arr[-d:]+arr[:-d]
# print(arr)