def convertLength(sourceUnit, targetUnit, value):
    # Conversion factors
    lengthUnits = {"cm": 1, "in": 2.54, "m": 100}

    if sourceUnit not in lengthUnits or targetUnit not in lengthUnits:
        return -1

    # Convert the source value to cm (base unit), then convert to the target unit
    return (value * lengthUnits[sourceUnit]) / lengthUnits[targetUnit]

def convertWeight(sourceUnit, targetUnit, value):
    # Conversion factors
    weightUnits = {"kg": 1, "lbs": 0.45359237, "st": 0.157473044}

    if sourceUnit not in weightUnits or targetUnit not in weightUnits:
        return -1

    # Convert the source value to kg (base unit), then convert to the target unit
    return (value * weightUnits[sourceUnit]) / weightUnits[targetUnit]

def superConversionFunction(sourceUnit, targetUnit, value):
    # Length units
    lengthUnits = ["cm", "in", "m"]

    # Weight units
    weightUnits = ["kg", "lbs", "st"]

    if sourceUnit in lengthUnits and targetUnit in lengthUnits:
        return convertLength(sourceUnit, targetUnit, value)
    elif sourceUnit in weightUnits and targetUnit in weightUnits:
        return convertWeight(sourceUnit, targetUnit, value)
    else:
        return -1

sourceUnit = input("Enter source unit: ")

targetUnit = input("Enter target unit: ")

value = float(input("Enter value: "))

result = superConversionFunction(sourceUnit, targetUnit, value)

if result == -1:
    print("Invalid conversion.")

else:
    print(f"{value} {sourceUnit} is {result} {targetUnit}.")

print("________________________________________________________________________")