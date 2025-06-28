#missing number in an array           leetcode=268
#ex a=[2,3,4,5] n=5 missing number is 3
#optimal
#1.sum approch

# arr=[1,2,4,5]
# n=len(arr)+1
# sum=(n*(n+1))/2
# sum2=0
# for i in range(0,len(arr)):
#     sum2+=arr[i]
# print(int(sum-sum2))

#xor approch
arr=[1,2,4,5]
n=len(arr)+1
xor1=0
xor2=0
for i in range(0,n-1):
    xor2=xor2^arr[i]
    xor1=xor1^(i+1)
xor1=xor1^n
print(xor1^xor2)
