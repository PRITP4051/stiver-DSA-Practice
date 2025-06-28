## # WAP to find whether the given number is an Armstrong number. (An Armstrong 
# number of three digits is an integer such that the sum of the cubes of its digits is 
# equal to the number itself. For example, 371 is an Armstrong number since 3^3 + 
# 7^3 + 1^3 = 371) 
n = int(input("Enter the number: "))
num = n
sum = 0

while num != 0:
    rem = num % 10
    sum += rem ** 3
    num //= 10

if sum == n:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")