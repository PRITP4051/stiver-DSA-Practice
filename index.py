a = [2, 3, 5, 1, 9]
n=len(a)
k = 10
left,right=0,0
sum=a[0]
maxi=0
while right<n:
    while left<=right and  sum>k:
        sum-=a[left]
        left+=1
    if sum==k:
        maxi=max(maxi,right-left+1)
    right += 1
    if right < n:
        sum += a[right]
print(maxi)


    