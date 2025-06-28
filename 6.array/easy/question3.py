#check if array is sorted or not
                                               #leetcode=1752
def Issorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

arr = list(map(int, input("enter array element(saperated by space): ").split()))
print(Issorted(arr))

