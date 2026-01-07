# 1. Conditions

# 1️⃣ Write a program to check whether a number is:
# positive
# negative
# or zero

num = int(input("Enter an integer to check whether its positive, negative or neutral: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2️⃣ Write a program to find the largest of two numbers.

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
if first > second:
    print("The greater number is: ", first)
elif first < second:
    print("The greater number is: ", second)
else:
    print("Both the numbers are equal.")

# 2. Operators

# 3️⃣ Write a program that demonstrates:
# addition
# subtraction
# multiplication
# division
# (using two numbers taken as input)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Addition of {num1} and {num2}: ", num1 + num2)
print(f"Subtraction of {num1} and {num2}: ", num1 - num2)
print(f"Multiplication of {num1} and {num2}: ", num1 * num2)
print(f"Division of {num1} and {num2}: ", num1 / num2)

# 4️⃣ Write a program to check if a number is:
# greater than 10 and
# less than 50

number = int(input("Enter a number to check whether it is greater than 10 and less than 50: "))
if number > 10 and number < 50:
    print("Yes, it is greater than 10 and less than 50.")
else:
    print("No, it is not between the given range.")

# 5️⃣ Take a number as input (string) and:
# convert it to integer
# convert it to float
# print all three values with their types

n = input("Enter a number: ")
print("original data type on input: ",type(n))
print("converting into int: ",type(int(n)))
print("converting into float: ",type(float(n)))


# 6️⃣ Write a program to print all even numbers between 1 and 20.
print("All even numbers between 1 and 20: ")
for i in range(1,20):
    if i%2 == 0:

        print(i)
