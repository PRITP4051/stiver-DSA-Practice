#linear search in array

def search(arr,n):

    for i in range(len(arr)):
        if arr[i]==n:
            print("found at index",i)
            break
    return -1
n=int(input("enter number to search:"))
arr=[1,2,3,4,5,6,7]
print(search(arr,n))