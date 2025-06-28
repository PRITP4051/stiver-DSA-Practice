#check string is palindrome or not
# check string is palindrome or not            #leetcode=125
def rev(i):
    if i >= len(a) // 2:
        return True
    if a[i] != a[len(a) - i - 1]:
        return False
    return rev(i + 1)

a = input("Enter string: ")
print(rev(0))


            