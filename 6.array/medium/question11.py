#rotate image/matrix by 90 degree (matrix)        #leetcode=48
# brute force
# a=[[1,2,3,],[4,5,6],[7,8,9]]
# n=len(a)
# ans = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         ans[j][(n-1)-i]=a[i][j]
# for row in ans:
#     print(row)


#better +optimal

a=[[1,2,3,],[4,5,6],[7,8,9]]
n=len(a)
for i in range(0,n-1):
    for j in range(i+1,n):
        a[i][j],a[j][i]=a[j][i],a[i][j]
for i in range(n):
    a[i].reverse()
    print(a[i])
