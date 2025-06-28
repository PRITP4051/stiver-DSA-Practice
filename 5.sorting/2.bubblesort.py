#wap to performe bubble sort method to sort and array
arr = list(map(int, input("Enter array elements (space-separated): ").split()))
n=len(arr)
for i in range(n-1,0,-1):
    for j in range(0,i):   #run till i-1
        if (arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

    


