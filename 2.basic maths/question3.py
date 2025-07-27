# palindrome number                             #leetcode 9
n=int(input("enter the number:"))
num=n
sum=0
while n!=0:
    rem=n%10
    sum=(sum*10)+rem
    n//=10
if sum==num:
    print(num,"is the palindrome number")
else:
    print(num,"is not palindrome number")
    