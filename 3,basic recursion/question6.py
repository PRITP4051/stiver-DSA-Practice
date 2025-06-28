#sum of first n natural number using recursion

#main method by striver
#1.parameter way
def sum_n(i,sum):
    if i<1:
        print(sum)
        return
    sum_n(i-1,sum+i)
n=int(input("enter n: "))
sum_n(n,0)

#my method
#2.functional way
def sum_n(n):
    if n==0:
        return 0
    return n+sum_n(n-1)
print(sum_n(5))
