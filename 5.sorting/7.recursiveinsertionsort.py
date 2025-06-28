def insertion_sort(arr, i, n):
    # Base Case: i == n
    if i == n:
        return
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
    insertion_sort(arr, i + 1, n)

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
n = len(arr)
print("Before Using insertion sort:")
print(arr)
insertion_sort(arr, 0, n)
print("After Using insertion sort:")
print(arr)

