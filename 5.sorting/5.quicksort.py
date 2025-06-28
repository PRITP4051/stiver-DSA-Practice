def quick(arr, low, high):
    pivot = arr[low]
    i = low                               #leetcode=912
    j = high
    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort(arr, low, high):
    if low < high:
        partition = quick(arr, low, high)
        quicksort(arr, low, partition - 1)
        quicksort(arr, partition + 1, high)

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)