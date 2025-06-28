#intersection on two array
#brute force
# a=[1,2,2,3,3,4,5,6]
# b=[2,3,3,5,6,6,7]
# n1=len(a)
# n2=len(b)
# vis=[0]*n2
# ans=[]
# for i in range(n1):
#     for j in range(n2):
#         if a[i]==b[j] and vis[j]==0:
#             ans.append(a[i])
#             vis[j]=1
#             break
#         if b[j]>a[i]:
#             break
# print(ans)

#optimal

a=[1,2,2,3,3,4,5,6]
b=[2,3,3,5,6,6,7]
n1=len(a)
n2=len(b)
ans=[]
i=0
j=0
while i<n1 and j<n2:
    if a[i]==b[j]:
        ans.append(a[i])
        i+=1
        j+=1
    elif a[i]<b[j]:
        i+=1
    else:
        j+=1
print(ans)
