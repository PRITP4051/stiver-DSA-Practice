#2 sum problem ex a=[2,7,9,11] and k=9                leetcode=1
#ans [0,1]

#brute force
# a = [2, 7, 9, 11]
# k = 9
# n = len(a)
# r = []

# for i in range(n):
#     for j in range(i + 1, n):  # Check pairs
#         if a[i] + a[j] == k:
#             r.append(i)
#             r.append(j)
#             break  # Stop after finding the first pair

# print(r)

# better=hashing         and optimal also
def two_sum(a, k):
    num_map = {}  # Hashmap to store numbers and their indices
    for i, num in enumerate(a):
        complement = k - num
        if complement in num_map:
            return [num_map[complement], i]  # Return indices of the two numbers
        num_map[num] = i  # Store the current number's index
    return []  # Return empty list if no pair is found

# Example usage
a = [2, 7, 9, 11]
k = 18
result = two_sum(a, k)
print(result)








