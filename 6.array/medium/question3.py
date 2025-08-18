# Majority element in array (>n/2 times)
#brute force
# a=[2,2,3,3,1,2,2]                       #leetcode =169
# n=len(a)
# for i in range(n):
#     count=0
#     for j in range(n):
#         if a[i]==a[j]:
#             count+=1
# if count>n/2:
#     print(a[i])
#better
from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)
    print(counter)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)

#optimal

def majorityElement(arr):
    # Size of the given array
    n = len(arr)
    cnt = 0  # Count
    el = None  # Element

    # Applying the algorithm
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    # Checking if the stored element is the majority element
    cnt1 = 0
    for i in range(n):
        if arr[i] == el:
            cnt1 += 1

    if cnt1 > (n / 2):
        return el
    return -1
arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)

