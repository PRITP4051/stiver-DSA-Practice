# spiral matrix                      #leetcode=54
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
ans=[]
n=len(a)
m=len(a[0])
left,right=0,m-1
top,bottom=0,n-1
#right
while top<=bottom and left<=right:

    for i in range(left,right+1):
        ans.append(a[top][i])
    top+=1
    #bottom
    for i in range(top,bottom+1):
        ans.append(a[i][right])
    right-=1
    #left
    if top<=bottom:
        for i in range(right,left-1,-1):
            ans.append(a[bottom][i])
        bottom-=1
    #top
    if left<=right:
        for i in range(bottom,top-1,-1):
            ans.append(a[i][left])
        left+=1
print(ans)

