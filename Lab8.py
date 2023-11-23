#task 8.1
import math

def computeArea(radius):
    area = math.pi * radius ** 2
    return area

#task 8.2
def classifyMark(mark):
    if mark < 40:
        return "Fail"
    elif mark < 50:
        return "Third"
    elif mark < 60:
        return "2(ii)"
    elif mark < 70:
        return "2(i)"
    else:
        return "First"

#task 8.3

import random

def printRandomJoke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why don't some fish play piano? Because you can't tuna fish!"
    ]

    print(random.choice(jokes))

#challenge task 8.4
def printRandomJoke2(name):
    jokes = [
        f"Why did {name} go to school? Because they couldn't find the right angle!",
        "Why don't scientists trust atoms? Because they make up everything!",
        f"Why did {name} bring a ladder to the bar? Because they heard the drinks were on the house!"
    ]

    print(random.choice(jokes))

#challenge task 8.5
def fibonacci(n):
    # The first two numbers in the Fibonacci sequence are 0 and 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Each subsequent number is the sum of the previous two
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return a

def main():
    #task 8.1
    print("Area of a circle with radius 1: ", computeArea(1))
    print("Area of a circle with radius 2: ", computeArea(2))
    print("Area of a circle with radius 3: ", computeArea(3))

    #task 8.2
    mark = float(input("Please enter a student's mark: "))

    classification = classifyMark(mark)

    print("The classification of the mark is: ", classification)

    #task 8.3
    for _ in range(3):
        printRandomJoke()

    #challenge task 8.4
    name = input("Please enter a name: ")

    for _ in range(3):
        printRandomJoke2(name)

    #challenge task 8.5
    n = int(input("Please enter a number: "))
    print(fibonacci(n))
if __name__ == "__main__":
    main()
