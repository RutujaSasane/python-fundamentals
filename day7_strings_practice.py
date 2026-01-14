# Q1. Count words in a sentence
# Take a sentence as input and count how many words it has.
# Example:
# Input: Python is very powerful
# Output: Number of words: 4

s1 = input("Enter a sentence to count how many words it has: ")

s = s1.split()
print(f"Number of words: {len(s)}")

# Q2. Find the longest word in a sentence
# Take a sentence as input and print the longest word.
# Example:
# Input: Python programming is fun
# Output: programming

s2 = input("Enter a sentence to print the longest word it has: ")

words = s2.split()

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

# Q3. Check if two strings are equal ignoring case and spaces
# Take two strings and check if they are the same, ignoring:
# case differences
# extra spaces

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

s1_1 = s1.replace(" ","")
s2_2 = s2.replace(" ","")

if s1_1.lower() == s2_2.lower():
    print("they are equal.")
else:
    print("they are unequal.")

# Q4. Replace vowels with *
# Take a string and replace all vowels with *.
# Example:
# Input: hello
# Output: h*ll*

string = input("enter a string to replace all vowels with *:")
s = ""
for ch in string:
    if ch.lower() in "aeiou":
        s += "*"
    else:
        s += ch
print("the result is:", s)

# Q5. Print first non-repeating character
# Take a string and print the first character that does not repeat.
# Example:
# Input: aabccd
# Output: b

s5 = input("Enter a string to print the first character that does not repeat:")
freq = {}

for s in s5:
    if s in freq:
        freq[s] += 1
    else:
        freq[s] = 1
        
for ch in s5:
    if freq[ch] == 1:
        print("First non-repeating charcter is: ", ch)
        break

# Q6. Check whether a string contains only digits.
# Example:
# "12345" → Yes
# "12a45" → No

s6 = input("Enter a string to check whether it contains only digits: ")

if all('0' <= ch <= '9' for ch in s6):
    print("yes")
else:
    print("no")