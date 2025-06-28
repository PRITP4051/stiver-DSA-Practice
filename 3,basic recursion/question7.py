#factorial of n using recursion
#1.parameter wat
# def fact_n(i,factorial):
#     if i==0:
#         print("factorial of",n,"is: ",factorial)
#         return
#     fact_n(i-1,factorial*i)              #4*3*2*1
# n=int(input("enter n: "))
# fact_n(n,1)

#2.functional way

def fact_n(n):                                 
    if n==0:
        return 1
    return n*fact_n(n-1)
n=int(input("enter n: "))
print("factorial of",n,"is: ",fact_n(n))

