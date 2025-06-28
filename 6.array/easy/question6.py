#left rotate an array by d times

# brute force solution
arr = list(map(int, input("enter array element(saperated by space): ").split()))
n = len(arr)
d = int(input("Enter k (number of rotations): "))
d = d % n  # To handle cases where k > n
temp=[]
for i in range(0,d):
    temp.append(arr[i])
for i in range(d,n):
    arr[i-d]=arr[i]
for i in range(n-d,n):
    arr[i]=temp[i-(n-d)]
print(arr)

#optimal solution

# def reverse_subarray(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1

# arr = list(map(int, input("enter array element(saperated by space): ").split()))
# n = len(arr)
# d = int(input("Enter k (number of rotations): "))
# d = d % n  # To handle cases where k > n

# reverse_subarray(arr, 0, d - 1)
# reverse_subarray(arr, d, n - 1)
# reverse_subarray(arr, 0, n - 1)

# print(arr)


#thinking sollution

arr = list(map(int, input("enter array element(saperated by space): ").split()))
n = len(arr)
d = int(input("Enter k (number of rotations): "))
d = d % n  # To handle cases where k > n
arr=arr[d:]+arr[:d]
print(arr)
