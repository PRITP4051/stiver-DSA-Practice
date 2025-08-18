#pascal triangle      #leetcode=118
# varity1
# import math

# def nCr(n, r):
#     res = 1

#     # calculating nCr:
#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)

#     return res

# def pascalTriangle(r, c):
#     element = nCr(r - 1, c - 1)
#     return element

# if __name__ == '__main__':
#     r = 5 # row number
#     c = 3 # col number
#     element = pascalTriangle(r, c)
#     print(f"The element at position (r,c) is: {element}")
    

#varity2
# def pascalTriangle(n):
#     ans = 1
#     print(ans, end=" ") # printing 1st element

#     #Printing the rest of the part:
#     for i in range(1, n):
#         ans = ans * (n - i)
#         ans = ans // i
#         print(ans, end=" ")
#     print()

# if __name__ == "__main__":
#     n = 5
    # pascalTriangle(n)

# varity3

from typing import *

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()
        