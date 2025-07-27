# #3 sum                          #leetcode=15
# # a[i]+a[j]+a[k]=0
# # i!=j!=k

# #brute force

# a=[-1,0,1,2,-1,-4]
# st=set()
# n=len(a)
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if a[i]+a[j]+a[k]==0:
#                 temp = [a[i], a[j], a[k]]
#                 temp.sort()
#                 st.add(tuple(temp))
# # store the set elements in the answer:
# ans = [list(item) for item in st]
# print(ans)


# #better

# def triplet(n, arr):
#     st = set()

#     for i in range(n):
#         hashset = set()
#         for j in range(i + 1, n):
#             # Calculate the 3rd element:
#             third = -(arr[i] + arr[j])

#             # Find the element in the set:
#             if third in hashset:
#                 temp = [arr[i], arr[j], third]
#                 temp.sort()
#                 st.add(tuple(temp))
#             hashset.add(arr[j])

#     # store the set in the answer:
#     ans = list(st)
#     return ans


# arr = [-1, 0, 1, 2, -1, -4]
# n = len(arr)
# ans = triplet(n, arr)
# for it in ans:
#     print("[", end="")
#     for i in it:
#         print(i, end=" ")
#     print("]", end=" ")
# print()


#optimal
nums=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
nums.sort()
n=len(nums)
ans=[]
for i in range(n):
    if (i!=0 and nums[i]==nums[i-1]):
        continue
    j=i+1
    k=n-1
    while j<k:
        if nums[i]+nums[j]+nums[k]<0:
            j+=1
        elif nums[i]+nums[j]+nums[k]>0:
            k-=1
        else:
            temp=[nums[i], nums[j], nums[k]]  # Fixed: individual elements, not sum
            ans.append(temp)
            j+=1
            k-=1
            while(j<k and nums[j]==nums[j-1]):
                j+=1
            while(j<k and nums[k]==nums[k+1]):  # Fixed: k-1 instead of k+1
                k-=1
print(ans)

