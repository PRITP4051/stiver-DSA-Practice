#reverse an array
def rev(i):
    if i >= n // 2:
        return
    a[i], a[n - i - 1] = a[n- i - 1], a[i]
    rev(i + 1)
n=int(input("enter array length: "))
a = list(map(int, input("Enter numbers separated by space: ").split()))
print("Array:", a)
rev(0)
print("Reversed array:", a)


#no build in function in python for swapping an element
