#4 sum                         #leetcode=18
# a[i]+a[j]+a[k]+a[l]=0
# i!=j!=k!=l

# #brute force
# a=[1,0,-1,0,-2,2]
# st=set()
# n=len(a)
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 sum=a[i]+a[j]
#                 sum+=a[k]
#                 sum+=a[l]
#                 if sum==0:
#                     temp = [a[i], a[j], a[k],a[l]]
#                     temp.sort()
#                     st.add(tuple(temp))
# # store the set elements in the answer:
# ans = [list(item) for item in st]
# print(ans)

# #bettter solution
# arr=[1,0,-1,0,-2,2]
# n=len(arr)
# st = set()

# for i in range(n):
    
#     for j in range(i + 1, n):
#         hashset = set()
#         for k in range(j+1,n):
            
#             # Calculate the 3rd element:
#             forth = -(arr[i] + arr[j]+arr[k])
#             # Find the element in the set:
#             if forth in hashset:
#                 temp = [arr[i], arr[j],arr[k], forth]
#                 temp.sort()
#                 st.add(tuple(temp))
#             hashset.add(arr[k])

# # store the set in the answer:
# ans = list(st)
# print(ans)


#optimal
nums=[1,0,-1,0,-2,2]
target=int(input("enter target:"))
nums.sort()
n=len(nums)
ans=[]
for i in range(n):
    if (i>0 and nums[i]==nums[i-1]):
        continue
    for j in range(i+1,n):
        # avoid the duplicates while moving j:
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            sum=nums[i]+nums[j]+nums[k]+nums[l]
            if sum<target:
                k+=1
            elif sum>target:
                l-=1
            else:
                temp=[nums[i], nums[j], nums[k],nums[l]]  # Fixed: individual elements, not sum
                ans.append(temp)
                k+=1
                l-=1
                while(k<l and nums[k]==nums[k-1]):  # Fixed: k-1 instead of k+1
                    k+=1
                while(k<l and nums[l]==nums[l+1]):  # Fixed: k-1 instead of k+1
                    l-=1  

print(ans)

