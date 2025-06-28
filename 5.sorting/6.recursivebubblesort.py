def recursivebubblesort(arr, n):
    if n == 1:
        return
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursivebubblesort(arr, n - 1)

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
n = len(arr)
recursivebubblesort(arr, n)
print("Sorted array:", arr)