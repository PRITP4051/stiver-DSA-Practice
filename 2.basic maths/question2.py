#reverse of a number          #leetcode=7
num =int(input("Enter The Number: "))
reversed_num = 0
while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit         #in number format
        num //= 10

print("Reversed Number: ", reversed_num)
