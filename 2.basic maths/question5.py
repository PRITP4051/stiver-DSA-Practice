#print all devision
import math as m
n=int(input("enter number:"))
list=[]
for i in range(1,int(m.sqrt(n)+1)):
    if(n%i==0):
        list.append(i)
        if((n/i)!=i):
            list.append(int(n/i))
list.sort()
print("sorted list",list)