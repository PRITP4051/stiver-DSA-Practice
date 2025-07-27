#longest subarray with sum 0
a = [1,-1,3, 2, -2, -8, 1, 7, 10, 23]
n=len(a)
preSumMap = {}
Sum = 0
maxLen = 0
for i in range(n):
    # calculate the prefix sum till index i:
    Sum += a[i]

    # if the sum = k, update the maxLen:
    if Sum == 0:
        maxLen = max(maxLen, i + 1)

    # calculate the sum of remaining part i.e. x-k:
    rem = Sum

    # Calculate the length and update maxLen:
    if rem in preSumMap:
        length = i - preSumMap[rem]
        maxLen=max(maxLen,length)
    
    # Finally, update the map checking the conditions:
    if Sum not in preSumMap:
        preSumMap[Sum] = i
print(maxLen)
