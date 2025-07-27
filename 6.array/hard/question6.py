# count subarray with xor as k

a=[4,2,2,6,4]
k = 6
n = len(a)
count = 0
prefix_xor = 0
freq = {0: 1}

for num in a:
    prefix_xor ^= num
    count += freq.get(prefix_xor^k, 0)
    freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
print(count)  # Output: 4

