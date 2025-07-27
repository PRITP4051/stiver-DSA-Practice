#rearrange array elements by sign
                                                 #leetcode=2149
#brute force
# arr=[3,1,-2,-5,2,-4]
# pos=[]
# neg=[]
# for i in arr:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# for i in range(len(arr)//2):
#     arr[i*2]=pos[i]
#     arr[(i*2)+1]=neg[i]
# print(arr)

#optimal

# arr=[3,1,-2,-5,2,-4]
# posindex=0
# negindex=1
# ans=[0]*len(arr)
# for i in range(len(arr)):
#     if arr[i]>0:
#         ans[posindex]=arr[i]
#         posindex+=2
#     else:
#         ans[negindex]=arr[i]
#         negindex+=2
# print(ans)


#varity 2 where no of positive != no of negetive
# method 1
# arr=[3,1,2,-5,2,-4]
# pos=[]
# neg=[]
# for i in arr:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# for i in range(min(len(pos),len(neg))):
#     arr[i*2]=pos[i]
#     arr[(i*2)+1]=neg[i]
# idx=max(len(pos),len(neg))
# for i in range(min(len(pos),len(neg)),idx):
#     arr[idx]=pos[i]
#     idx+=1
# print(arr)

# method 2

arr=[3,1,-2,-5,-2,-4]
pos=[]
neg=[]
for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
if len(pos)>len(neg):
    for i in range(len(neg)):
        arr[i*2]=pos[i]
        arr[(i*2)+1]=neg[i]
    idx=len(neg)*2
    for i in range(len(neg),len(pos)):
        arr[idx]=pos[i]
        idx+=1
else:
    for i in range(len(pos)):
        arr[i*2]=pos[i]
        arr[(i*2)+1]=neg[i]
    idx=len(pos)*2
    for i in range(len(pos),len(neg)):
        arr[idx]=neg[i]
        idx+=1
print(arr)