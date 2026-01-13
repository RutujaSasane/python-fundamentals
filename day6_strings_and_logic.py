# Q1. Count vowels and consonants in a string
# Take a string as input and count:
# number of vowels
# number of consonants
# Ignore spaces.
# Example:
# Input: hello world
# Output:
# Vowels: 3
# Consonants: 7

s = input("Enter a string to count the no. of vowels and consonants: ")
v = 0
c = 0
for s1 in s:
    if s1 == 'a' or s1 == 'e' or s1 == 'i' or s1 == 'o' or s1 == 'u':
        v += 1
    elif s1 == ' ':
        pass
    else:
        c += 1
print(f"No. of vowels: {v}")
print(f"No. of consonants: {c}")

# Q2. Reverse each word in a sentence

# Take a sentence as input and reverse each word, not the full sentence
# Example:
# Input: hello world
# Output: olleh dlrow

s2 = input("Enter a sentence to reverse each word in it: ")
words = s2.split()
result = []

for word in words:
    reverse = ""
    for char in word:
        reverse = char + reverse
    result.append(reverse)

print(" ".join(result))

# Q3. Check if a string is a palindrome (ignore case)

# Take a string as input and check if it is a palindrome.
# Ignore case differences

# Example:
# Madam → Palindrome
# Python → Not palindrome.

s3 = input("Give string as input and check if it is a palindrome, ignoring the case differences: ")
rev = ""
for s in s3.lower():
    rev = s + rev

if s3.lower() == rev.lower():
    print("palindrome")
else:
    print("not a palindrome")

# Q4. Find the frequency of each character
# Take a string and print how many times each character appears.

# Example:
# Input: aabcc
# Output:

# a : 2
# b : 1
# c : 2

s4 = input("Enter a string to print how many times each character appears: ")
freq = {}
for each in s4:
    if each in freq:
        freq[each] += 1
    else:
        freq[each] = 1
        
print(freq)
        
# Q5. Remove duplicate characters from a string

# Take a string and print it without duplicate characters, keeping the original order.

# Example:
# Input: programming
# Output: progamin

s5 = input("Enter a string to print it without duplicate characters:")
original = []
for ch in s5:
    if ch not in original:
        original.append(ch)
print("".join(original))

# Q6. Check whether two strings are anagrams of each other.

# Example:
# listen, silent → Anagram
# hello, world → Not anagram

print("Check whether two strings are anagrams of each other!!")
first = input("Enter first string: ").lower()
second = input("Enter second string: ").lower()

f = sorted(first)
s = sorted(second)

if f == s:
    print("Anagram")
else:
    print("Not an anagram")