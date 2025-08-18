#maximum subarray sum 
#kadane's algorithm                 #leetcode=53
#brute force
a=[-2,-3,4,-1,-2,1,5,-3]
n=len(a)
maxi=10**-5
for i in range(n):
    for j in range(i,n):
        sum=0
        for k in range(i,j):
            sum+=a[k]
        maxi=max(maxi,sum)
print(maxi)


#better 
a=[-2,-3,4,-1,-2,1,5,-3]
n=len(a)
maxi=10**-5
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=a[j]
        maxi=max(maxi,sum)
print(maxi)

#optimal solution
import sys
a=[-2,-3,4,-1,-2,1,5,-3]
n=len(a)
maxi=-sys.maxsize
sum=0
for i in range(n):
    sum+=a[i]
    maxi=max(sum,maxi)
    if sum<0:
        sum=0
print(maxi)

#for that subarray print
a=[-2,-3,4,-1,-2,1,5,-3]
n=len(a)
maxi=-10**5
sum=0
ansstart,ansend=-1,-1
for i in range(n):
    if sum==0:
        start=i
    sum+=a[i]
    if sum>maxi:
        maxi=sum
        ansstart=start
        ansend=i
    if sum<0:
        sum=0
list=[]
for i in range(ansstart,ansend+1):
    list.append(a[i])
print(list)

    

