#largest element in array
# arr=list(map(int,input("enter array element(saperated by space)").split()))
# n=len(arr)
# largest=arr[0]
# for i in range(0,n):
#     if arr[i]>largest:
#         largest=arr[i]
# print(largest)


#smallest element in the array
arr=list(map(int,input("enter array element(saperated by space)").split()))
n=len(arr)
smallest=arr[0]
for i in range(0,n):
    if arr[i]<smallest:
        smallest=arr[i]
print(smallest)