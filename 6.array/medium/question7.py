#next permutation              #leetcode=31
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=[3,2,1]
n=len(arr)
idx=-1

for i in range(n-2,-1,-1):
    if arr[i]<arr[i+1]:
        idx=i
        break
if idx == -1:
    # Entire array is non-increasing, reverse it to smallest permutation
    reverse(arr, 0, n - 1)
    print(arr)

for i in range(n-1,idx-1,-1):
    if arr[i]>arr[idx]:
        arr[i],arr[idx]=arr[idx],arr[i]
        break
reverse(arr,idx+1,n-1)
print(arr)
