# Q1. Count digits in a number
# Take a number as input and count how many digits it has.
# Example:
# Input: 4589
# Output: Number of digits: 4
# (Use a loop, not string conversion)

num = input("Enter a number to count the no. of digits it has: ")
count = 0
for n in num:
    count = count+1
print(f"Number of digits in {num}: ", count)

# Q2. Reverse a number
# Take a number as input and print its reverse.
# Example:
# Input: 1234
# Output: 4321
num1 = input("Enter a number to print its reverse: ")
char = ""
for n1 in num1:
    char = n1 + char
print("reversed number: ", char)

# Q3. Sum of digits
# Take a number as input and find the sum of its digits.
# Example:
# Input: 248
# Output: Sum = 14

num2 = input("Enter number to find sum of its digits: ")
sum = 0
for n2 in num2:
    sum += int(n2)
print("Sum: ", sum)

# Q4. Prime number check
# Take a number as input and check whether it is prime or not.

num3 = int(input("Enter a number to check whether it is prime or not: "))

if num3 < 1:
    print("Not a prime number.")
elif num3 == 1:
    print("1 is neither prime nor composite number.")
else:
    is_prime = True
    for i in range(2, num3):
        if num3 % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

# Q5. Print a pattern (logic + loops)
# Print the following pattern for n = 5:
# *
# **
# ***
# ****
# *****
num4 = int(input("Enter a number: "))
for i in range(1, num4+1):
    print("*" * i)

# Q6. Bonus (only if energy remains)
# Print all numbers between 1 and 100 that are divisible by 3 and 5.
for i in range(1,101):
    if (i%3 == 0) and (i%5 == 0):
        print(i)

