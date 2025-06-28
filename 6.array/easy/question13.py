#maximum consecutive one's in binary number array        #leetcode=485
arr=[1,1,0,1,1,1,0,1,1,1,1,0,0,1]
max1=0
cnt=0
for i in range(0,len(arr)):
    if arr[i]==1:
        cnt+=1
        max1=max(max1,cnt)
    else:
        cnt=0
print(max1)