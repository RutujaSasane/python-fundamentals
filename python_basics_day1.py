# Write a program to:
# take input
# check even / odd
num = int(input("Enter a number to check if its even or odd: "))
if num % 2 == 0:
    print("Its an even number.")
else:
    print("Its an odd number.")
# Write a program to:
# swap two numbers (with temp & without temp)
# with temp
a = 10
b = 20
print("before swapping")
print("value of a: ",a)
print("value of b: ",b)

temp = a
a = b
b = temp

print("after swapping")
print("value of a: ",a)
print("value of b: ",b)

# without temp
a = 10
b = 20
print("before swapping")
print("value of a: ",a)
print("value of b: ",b)

a = a + b
b = a - b
a = a - b
print("after swapping")
print("value of a: ",a)
print("value of b: ",b)

# Write a program to:
# take a string and print its length
s = input("Enter a string to find its length: ")
print("Length of the string is: ", len(s))
print("Length of the string is: ", s.count("")-1)

# Bonus (only if energy remains):
# print numbers 1 to 10 using a loop
for i in range(1,11):
    print(i)