#count subarray with given sum    #leetcode=560
# bruteforce+better
# a=[1,1,1,1]
# k=2
# n=len(a)
# count=0
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         sum+=a[j]
#         if sum==k:
#             count+=1
# print(count)

#optimal

a = [1, 1, 1, 1]
k = 2
n = len(a)
count = 0
prefix_sum = 0
freq = {0: 1}

for num in a:
    prefix_sum += num
    count += freq.get(prefix_sum - k, 0)
    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

print(count)  # Output: 3



