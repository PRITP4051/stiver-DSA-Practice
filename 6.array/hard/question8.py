# #merge two sorted arrays without enxtra space    #leetcode=88
# #brute force
# def merge(arr1, arr2, n, m):

#     # Declare a 3rd array and 2 pointers:
#     arr3 = [0] * (n + m)
#     left = 0
#     right = 0
#     index = 0

#     # Insert the elements from the 2 arrays
#     # into the 3rd array using left and right
#     # pointers:
#     while left < n and right < m:
#         if arr1[left] <= arr2[right]:
#             arr3[index] = arr1[left]
#             left += 1
#             index += 1
#         else:
#             arr3[index] = arr2[right]
#             right += 1
#             index += 1

#     # If right pointer reaches the end:
#     while left < n:
#         arr3[index] = arr1[left]
#         left += 1
#         index += 1

#     # If left pointer reaches the end:
#     while right < m:
#         arr3[index] = arr2[right]
#         right += 1
#         index += 1

#     # Fill back the elements from arr3[]
#     # to arr1[] and arr2[]:
#     for i in range(n + m):
#         if i < n:
#             arr1[i] = arr3[i]
#         else:
#             arr2[i - n] = arr3[i]

# if __name__ == '__main__':
#     arr1 = [1, 4, 8, 10]
#     arr2 = [2, 3, 9]
#     n = 4
#     m = 3
#     merge(arr1, arr2, n, m)

#     print("The merged arrays are:")
#     print("arr1[] = ", end="")
#     for i in range(n):
#         print(arr1[i], end=" ")
#     print("\narr2[] = ", end="")
#     for i in range(m):
#         print(arr2[i], end=" ")
#     print() 


#optimal


# arr1 = [1, 3,5,7]
# arr2 = [0,2,6,8,9]
# n=len(arr1)
# m=len(arr2)
# left,right=n-1,0
# while left >= 0 and right < m:
#         if arr1[left] > arr2[right]:
#             arr1[left], arr2[right] = arr2[right], arr1[left]
#             left -= 1
#             right += 1
#         else:
#             break
# arr1.sort()
# arr2.sort()
# print(arr1)
# print(arr2) 


#optimal 2
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
n = len(arr1)
m = len(arr2)
total_len = n + m

# Initial gap:
gap = (total_len // 2) + (total_len % 2)

while gap > 0:
    # Place 2 pointers:
    left = 0
    right = left + gap
    while right < total_len:
        # case 1: left in arr1[] and right in arr2[]:
        if left < n and right >= n:
            if arr1[left] > arr2[right - n]:  # <-- ADDED COMPARISON
                arr1[left], arr2[right - n] = arr2[right - n], arr1[left]
        # case 2: both pointers in arr2[]:
        elif left >= n:
            if arr2[left - n] > arr2[right - n]:  # <-- ADDED COMPARISON
                arr2[left - n], arr2[right - n] = arr2[right - n], arr2[left - n]
        # case 3: both pointers in arr1[]:
        else:
            if arr1[left] > arr1[right]:  # <-- ADDED COMPARISON
                arr1[left], arr1[right] = arr1[right], arr1[left]
        
        left += 1
        right += 1
        
    # break if iteration gap=1 is completed:
    if gap == 1:
        break
        
    # Otherwise, calculate new gap:
    gap = (gap // 2) + (gap % 2)

print("Merged arr1:", arr1)
print("Merged arr2:", arr2)