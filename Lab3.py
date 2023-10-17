#task 3.1
name = input("What is your name? ")

numberInRow = int(input("How many people are in your row in the lab? "))

neighbourName = input("What is your neighbour's name? ")

print("Hello %s. You are one of %d people in this row.\nYour neighbour is %s." % (name, numberInRow, neighbourName))
print("________________________________________________________________________")
#task 3.2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
print("Sum:", sum)

difference = num1 - num2
print("Difference:", difference)

product = num1 * num2
print("Product:", product)

average = sum / 2
print("Average:", average)

distance = abs(difference)
print("Distance:", distance)

maximum = max(num1, num2)
print("Maximum:", maximum)

minimum = min(num1, num2)
print("Minimum:", minimum)
print("________________________________________________________________________")
#task 3.3
price_per_drink = float(input("What is the price per drink? "))

num_drinks = int(input("How many drinks have you purchased this week? "))

total_cost = price_per_drink * num_drinks

print("The total cost of your drinks this week is: %.2f" % total_cost)
print("________________________________________________________________________")
#task 3.4
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

initial = firstName[0]

print("Your initial and last name is: %s.%s" % (initial, lastName))
print("________________________________________________________________________")
#challenge task 3.5
box_size = int(input("Enter the size of the box: "))

print("*" * box_size)

for i in range(box_size - 2):
    print("*" + " " * (box_size - 2) + "*")

print("*" * box_size)

