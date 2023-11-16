#task 7.1
for i in range(10, 0, -1):
    print(i)

print("----")

for i in range(2, 21, 2):
    print(i)

print("________________________________________________________________________")
#task 7.2
evenCount = 0
oddCount = 0

while True:
    x = int(input("Please enter an integer (or 0 to stop): "))

    if x == 0:
        break

    if x % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print("Number of even numbers: ", evenCount)
print("Number of odd numbers: ", oddCount)

print("________________________________________________________________________")
#task 7.3
s = input("Please enter a string: ")

vowelCount = 0

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in s:
    if char in vowels:
        vowelCount += 1

print("Number of vowels: ", vowelCount)

print("________________________________________________________________________")
#task 7.4
import random

for i in range(10):
    toss = random.randint(0, 1)

    if toss == 0:
        print("Heads")
    else:
        print("Tails")

print("________________________________________________________________________")
#challenge task 7.5
vowelCount = 0
consonantCount = 0

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

while True:
    sentence = input("Please enter a sentence (or press enter to stop): ")

    if sentence == "":
        break

    for char in sentence:
        if char in vowels:
            vowelCount += 1
        elif char in consonants:
            consonantCount += 1

print("Number of vowels: ", vowelCount)
print("Number of consonants: ", consonantCount)

print("________________________________________________________________________")
print("challenge task 7.6")
n = int(input("Please enter a positive integer (greater than or equal to 1): "))

for i in range(1, n+1):
    for _ in range(n-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()

