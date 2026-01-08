# Q1. Largest of three numbers
# Write a program to take three numbers as input and print the largest number.

print("Checking largest among 3 integers taken as input.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is largest.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is largest.")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is largest.")
else:
    print("Enter valid numbers.")

# Q2. Check eligibility (real-world logic)
# Take age as input and:
# if age < 18 → print "Not eligible to vote"
# if age ≥ 18 → print "Eligible to vote"

age = int(input("Enter age to check voting eligibility: "))

if age < 18 and age > 0:
    print("You are not eligible.")
elif age >= 18:
    print("You are eligible.")
else:
    print("Enter valid age.")

# Q3. Grade classification
# Take marks (0–100) as input and print grade:
# ≥ 90 → A
# ≥ 75 and < 90 → B
# ≥ 50 and < 75 → C
# < 50 → Fail

marks = int(input("Enter marks of the student (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks < 90:
    print("Grade: B")
elif marks >= 50 and marks < 75:
    print("Grade: C")
elif marks < 50 and marks >= 0:
    print("Fail.")
else:
    print("Enter valid marks.")

# Q4. Nested condition (important)
# Take a number as input:
# if number > 0
# check whether it is even or odd
# else
# print "Number is not positive"

n = int(input("Enter a number: "))
if n > 0:
    if n%2 == 0:
        print("Even number.")
    else:
        print("Odd number.")
else:
    print("Number is not positive.")


# Q5. Bonus 
# Take two numbers and an operator (+, -, *, /) as input and perform the operation.
# (Simple calculator using conditionals)

print("Simple calculator using conditionals")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
o = input("Enter operator(+,-,*,/): ")

if o == "+":
    print("Ans: ", n1 + n2)
elif o == "-":
    print("Ans: ", n1 - n2)
elif o == "*":
    print("Ans: ", n1 * n2)
elif o == "/":
    print("Ans: ", n1 / n2)