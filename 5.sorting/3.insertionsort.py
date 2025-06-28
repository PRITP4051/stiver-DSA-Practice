#wap to perform insertion sort to sorting an array

# arr = list(map(int, input("Enter array elements (space-separated): ").split()))
# n=len(arr)
# for i in range(0,n):
#     for j in range(i,0,-1):      #run till >0 
#         if(arr[j-1]>arr[j]):
#             arr[j-1],arr[j]=arr[j],arr[j-1]
# print(arr)


#mathod 2
arr = list(map(int, input("Enter array elements (space-separated): ").split()))
n=len(arr)
for i in range(0,n):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)
