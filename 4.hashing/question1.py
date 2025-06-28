#hashing for numbers
# Define size of hash array
MAX = 10**7
hash_array = [0] * MAX

# Input array
arr = list(map(int, input("Enter array elements (space-separated): ").split()))

# Populate hash array
for num in arr:
    hash_array[num] += 1

# Input number of queries
q = int(input("Enter number of queries: "))

# Process each query
print("Enter queries (one per line):")
for _ in range(q):
    query = int(input())
    if 0 <= query < MAX:
        print(f"{query} appears {hash_array[query]} times")
    else:
        print(f"{query} is out of bounds")
