#hashing for a character string
MAX = 256
hash_array = [0] *256

# Input array
str=input("enter string:")

# Populate hash array
for char in str:
    hash_array[ord(char)] += 1

# Input number of queries
q = int(input("Enter number of queries: "))

# Process each query
print("Enter queries (one per line):")
for _ in range(q):
    query = input()
    if ord(query) < MAX:
        print(f"{query} appears {hash_array[ord(query)]} times")
    else:
        print(f"{query} is out of bounds")