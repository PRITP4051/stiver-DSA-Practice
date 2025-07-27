#longest sumarray with sum k [positive]

#brute wrost

# def getLongestSubarray(a, k):
#     n = len(a)
#     length = 0
#     for i in range(n):  # starting index
#         for j in range(i, n):  # ending index
#             s = 0
#             for K in range(i, j + 1):
#                 s += a[K]
#             if s == k:
#                 length = max(length, j - i + 1)
#     return length

# a = [2, 3, 5, 1, 9]
# k = 10
# length = getLongestSubarray(a, k)
# print(f"The length of the longest subarray is: {length}")


#brute force best
from typing import List

def getLongestSubarray(a: List[int], k: int) -> int:
    n = len(a)  # size of the array
    length = 0
    for i in range(n):  # starting index
        s = 0
        for j in range(i, n):  # ending index
            s += a[j]
            if s == k:
                length = max(length, j - i + 1)
                break
    return length

if __name__ == '__main__':
    a = [2, 3, 5, 1, 9]
    k = 10
    length = getLongestSubarray(a, k)
    print("The length of the longest subarray is:", length)

#better solutifrom typing import List

# def getLongestSubarray(a, k: int) -> int:
#     n = len(a)  # size of the array

#     preSumMap = {}
#     Sum = 0
#     maxLen = 0
#     for i in range(n):
#         # calculate the prefix sum till index i:
#         Sum += a[i]

#         # if the sum = k, update the maxLen:
#         if Sum == k:
#             maxLen = max(maxLen, i + 1)

#         # calculate the sum of remaining part i.e. x-k:
#         rem = Sum - k

#         # Calculate the length and update maxLen:
#         if rem in preSumMap:
#             length = i - preSumMap[rem]
#             maxLen=max(maxLen,length)
        
#         # Finally, update the map checking the conditions:
#         if Sum not in preSumMap:
#             preSumMap[Sum] = i

#     return maxLen

# if __name__ == "__main__":
#     a = [2, 3, 5, 1, 9]
#     k = 10

#     length = getLongestSubarray(a, k)
#     print(f"The length of the longest subarray is: {length}")

#optimal
from typing import List

def getLongestSubarray(a: List[int], k: int) -> int:
    n = len(a)  # size of the array

    left, right = 0, 0  # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n:
            Sum += a[right]

    return maxLen

if __name__ == "__main__":
    a = [2,-3, 5,0,1,9]
    k = 10

    length = getLongestSubarray(a, k)
    print(f"The length of the longest subarray is: {length}")