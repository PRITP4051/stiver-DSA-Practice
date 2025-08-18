#find how many times array is rotated
import sys

def count_rotations(nums):
    n = len(nums)
    low, high = 0, n - 1
    ans = sys.maxsize
    index = -1

    while low <= high:
        mid = (low + high) // 2

        # If the search space is already sorted,
        # the first element is the minimum.
        if nums[low] <= nums[high]:
            if nums[low] < ans:
                ans = nums[low]
                index = low
            break

        # If the left part is sorted
        if nums[low] <= nums[mid]:
            # Keep the minimum from this sorted part
            if nums[low] < ans:
                ans = nums[low]
                index = low
            # Eliminate the left part and look in the right
            low = mid + 1
        # If the right part is sorted
        else:
            # Keep the minimum from this sorted part
            if nums[mid] < ans:
                ans = nums[mid]
                index = mid
            # Eliminate the right part and look in the left
            high = mid - 1
            
    return index

# Example usage:
nums = [3, 4, 5, 1, 2]
rotations = count_rotations(nums)
print(f"The array is rotated {rotations} times.")

nums2 = [7, 8, 1, 2, 3, 4, 5, 6]
rotations2 = count_rotations(nums2)
print(f"The array is rotated {rotations2} times.")