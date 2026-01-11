# Q1. Check palindrome number
# Take a number as input and check whether it is a palindrome.
# Example:
# 121 → Palindrome
# 123 → Not palindrome

num1 = input("Enter a number to check whether it is palindrome: ")
rev_num1 = num1[::-1]

if num1 == rev_num1:
    print("It is palindrome.")
else:
    print("It is not palindrome")

# Q2. Print first n prime numbers
# Take n as input and print the first n prime numbers.
# Example:
# Input: 5
# Output: 2 3 5 7 11

num2 = int(input("Enter an input 'n' to print first n prime nos.: "))

count = 0
num = 2

while count < num2:
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1

# Q3. Factorial of a number (loops)
# Take a number as input and find its factorial.
# Example:
# Input: 5
# Output: 120

n = int(input("Enter a number to find its factorial: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f"factorial of {n} is {fact}")

# Q4. Pattern 
# Print this pattern for n = 5:
# *****
# ****
# ***
# **
# *

num4 = int(input("Enter a number: "))
for i in range(num4, 0, -1):
    print(i * "*")

# Q5. Count even and odd digits in a number
# Take a number as input and count:
# how many even digits
# how many odd digits

# Example:
# Input: 24861
# Even digits: 3
# Odd digits: 2

num5 = input("Enter a number to count its even and odd digits: ")
e = 0
o = 0
for i in num5:
    i = int(i)
    if i%2 == 0:
        e = e + 1 
    else:
        o = o + 1
print("even digits: ", e)
print("odd digits: ", o)

# Q6. Bonus (Siemens-style logic)
# Print all numbers between 1 and 50 that are:
# divisible by either 4 or 6
# but not both

print("Numbers between 1 and 50 that are divisible by either 4 or 6 but not both: ")
for i  in range(1, 51):
    if (i%4 == 0 or i%6 == 0) and not (i%4 == 0 and i%6 == 0):
        print(i)
        

