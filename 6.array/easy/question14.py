#find number which apperes ones while other numbers apperes twice in array
#n=[4,1,2,1,2] ans=4              #leetcode=136
arr = [4, 1, 2, 1, 2]
ans = 0
for num in arr:
    ans ^= num
print(ans)