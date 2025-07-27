#leaders in array   and=[22,12,6]
a=[10,22,12,3,0,6]
maxi=-10**7
n=len(a)
ans=[]
for i in range(n-1,-1,-1):
    if a[i]>maxi:
        maxi=a[i]
        ans.append(a[i])
print(ans)
        