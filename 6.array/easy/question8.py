#move zeroes to end in array
#brute force                               #leetcode=283
# arr = list(map(int, input("enter array element(saperated by space): ").split()))
# n = len(arr)
# temp=[]
# for i in range(0,n):
#     if arr[i]!=0:
#         temp.append(arr[i])
# for i in range(0,len(temp)):
#     arr[i]=temp[i]
# for i in range(len(temp),n):
#     arr[i]=0
# print(arr)

#optimal approch
arr = list(map(int, input("enter array element(saperated by space): ").split()))
n = len(arr)
j=-1
for i in range(0,n):
    if arr[i]==0:
        j=i
        break
if j!=-1:
    for i in range(j+1,n):
        if arr[i]!=0:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            j+=1
print(arr)