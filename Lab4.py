#task 4.1
age = int(input("Please enter your age in years: "))

if age >= 17:
    print("You are old enough to get a driving licence in the UK.")
else:
    print("You are not old enough to get a driving licence in the UK.")

print("________________________________________________________________________")
#task 4.2
name = input("Please enter the name of your lecturer: ")

if name.lower() == "jen":
    print("Jen teaches CSC061.")
else:
    print(f"{name} does not teach CSC061.")

print("________________________________________________________________________")
#task 4.3
POUND_TO_EURO = 1.10
EURO_TO_POUND = 0.91

print("Welcome to the Currency Converter")
print("")
print("1) Convert Pounds to Euro.")
print("2) Convert Euro to Pounds.")
choice = int(input("Which option would you like: "))
print("")

if choice == 1:
    pounds = float(input("Please enter the amount in Pounds: "))
    euros = pounds * POUND_TO_EURO
    print(f"{pounds} Pounds is {euros:.2f} in Euros")
elif choice == 2:
    euros = float(input("Please enter the amount in Euros: "))
    pounds = euros * EURO_TO_POUND
    print(f"{euros} Euros is {pounds:.2f} in Pounds")
else:
    print("Invalid option.")

print("________________________________________________________________________")
#challenge task 4.4
size = int(input("Please enter the size of the box: "))

boxType = input("Do you want a filled box or an empty box? ")

if boxType.lower() == "filled":
    for _ in range(size):
        print("*" * size)
elif boxType.lower() == "empty":
    print("*" * size)  # Top of the box
    for _ in range(size - 2):
        print("*" + " " * (size - 2) + "*")  # Middle of the box
    print("*" * size)  # Bottom of the box
else:
    print("Invalid option.")

print("________________________________________________________________________")
#challenge task 4.5
userString = input("Please enter a string: ")

boxLength = len(userString) + 4

print("*" * boxLength)
print("* " + userString + " *")
print("*" * boxLength)

print("________________________________________________________________________")
#challenge task 4.6
tempInput = input("Enter temperature: ")

temp = int(tempInput[:-1])
unit = tempInput[-1].upper()

if unit == 'C':
    if temp <= 0:
        print("Water is solid at this temperature.")
    elif temp <= 100:
        print("Water is liquid at this temperature.")
    else:
        print("Water is gaseous at this temperature.")
elif unit == 'F':
    if temp <= 32:
        print("Water is solid at this temperature.")
    elif temp <= 212:
        print("Water is liquid at this temperature.")
    else:
        print("Water is gaseous at this temperature.")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
