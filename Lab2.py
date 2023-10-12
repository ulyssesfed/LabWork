#task 2.1
age = 18

print("I am", age, "years old. in 2 years I will be", age+2,)
print("________________________________________________________________________")
#task 2.2
priceWithoutVat = float(input("Please enter the price of the item without VAT: "))

VatRate = 20  # VAT rate is typically 20% in the UK
vatAmount = (priceWithoutVat * VatRate) / 100
itemPriceWithVat = priceWithoutVat + vatAmount

print("VAT:", vatAmount)
print("Item price inc VAT:", itemPriceWithVat)
print("________________________________________________________________________")
#task 2.3
from math import sqrt

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))

hypotenuse = sqrt(side1**2 + side2**2)

print("The length of the hypotenuse is:", hypotenuse)
print("________________________________________________________________________")
#challenge task 2.4
celsius = float(input("Enter a temperature in degrees Celsius (C): "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
rankine = (celsius + 273.15) * 9/5

print("Temperature in degrees Fahrenheit (F):", fahrenheit)
print("Temperature in Kelvin (K):", kelvin)
print("Temperature in Rankine (R):", rankine)
print("________________________________________________________________________")
