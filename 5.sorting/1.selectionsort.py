#wap to perform selection method of sorting to array
arr = list(map(int, input("Enter array elements (space-separated): ").split()))
n=len(arr)
for i in range(0,n-1):
    min=i
    for j in range(i,n):
        if(arr[j]<arr[min]):
            min=j
    temp=arr[min]
    arr[min]=arr[i]
    arr[i]=temp
print(arr)

#you can swap two value by just doing this
#arr[i], arr[min] = arr[min], arr[i]
    
