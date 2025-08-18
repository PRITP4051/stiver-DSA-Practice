#print second largest element in array without sorting

# arr=list(map(int,input("enter array element(saperated by space): ").split()))
# n=len(arr)
# largest=arr[0]
# secondlargest=-1    #if array contain negative so write it in smaller value int min
# for i in range(0,n):
#     if(arr[i]>largest):
#         secondlargest=largest
#         largest=arr[i]
#     elif(arr[i]<largest and arr[i]>secondlargest):
#         secondlargest=arr[i]
# print(secondlargest)

#print second smallest element in array without sorting
import sys
arr=list(map(int,input("enter array element(saperated by space): ").split()))
n=len(arr)
smallest=arr[0]
secondsmallest=sys.maxsize  #if array contain negative so write it in larger value int max
for i in range(0,n):
    if(arr[i]<smallest):
        secondsmallest=smallest
        smallest=arr[i]
    elif(arr[i]!=smallest and arr[i]<secondsmallest):
        secondsmallest=arr[i]
print(secondsmallest)