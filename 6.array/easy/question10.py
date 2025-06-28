#union of two arrays

#brute force
# arr1=[1,1,2,3,4,5]
# arr2=[2,3,4,4,5,6]
# s=set()
# for i in range(len(arr1)):
#     s.add(arr1[i])
# for i in range(len(arr2)):
#     s.add(arr2[i])
# union=[]
# for i in s:
#     union.append(i)
# print("union",union)

#optimal
arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]
n1 = len(arr1)
n2 = len(arr2)
i = 0
j = 0
Union = []

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        if len(Union) == 0 or Union[-1] != arr1[i]:
            Union.append(arr1[i])
        i += 1
    else :
        if len(Union) == 0 or Union[-1] != arr2[j]:
            Union.append(arr2[j])
        j += 1

while i < n1:
    if len(Union) == 0 or Union[-1] != arr1[i]:
        Union.append(arr1[i])
    i += 1

while j < n2:
    if len(Union) == 0 or Union[-1] != arr2[j]:
        Union.append(arr2[j])
    j += 1

print(Union)
    

