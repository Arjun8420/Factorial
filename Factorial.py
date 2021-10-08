#Program to calculate the factorial of a number

num = int(input("Enter the Number = "))
res = 1

for x in range(1, num+1):
    res *= x

print("Factorial of ",num, "=", res)
