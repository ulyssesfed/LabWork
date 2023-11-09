#task 6.1
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

counter = 10
while counter >= 1:
    print(counter)
    counter -= 1

print("________________________________________________________________________")
#task 6.2
counter = 0
totalSum = 0

while counter <= 10:
    totalSum += counter
    counter += 1

print(totalSum)

print("________________________________________________________________________")
#task 6.3
counter = 1
totalSum = 0

while counter <= 10:
    number = float(input('Enter number %d: ' % counter))
    totalSum += number
    counter += 1

average = totalSum / 10

print('Average: %.2f' % average)

print("________________________________________________________________________")
#task 6.4
word = input("Enter a word: ")

start = 0
end = len(word) - 1

while start < end:
    if word[start] != word[end]:
        print("The word is not a palindrome.")
        break
    start += 1
    end -= 1
else:
    print("The word is a palindrome.")

print("________________________________________________________________________")
#challenge task 6.5
counter = 0
totalSum = 0

while True:
    number = float(input('Enter number or -1 to stop: '))
    if number == -1:
        break
    totalSum += number
    counter += 1

if counter > 0:
    average = totalSum / counter

    print('Average: %.2f' % average)
else:
    print('No numbers were entered.')

print("________________________________________________________________________")