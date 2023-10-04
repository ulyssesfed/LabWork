print("Which lab would you like to run?")
lab_number = input()  # Remove the unnecessary int() conversion

# Build the filename based on the user's input
filename = f"Lab{lab_number}.py"

try:
    with open(filename) as f:
        code = f.read()
        exec(code)
except FileNotFoundError:
    print(f"Lab{lab_number}.py not found.")
except Exception as e:
    print(f"An error occurred: {e}")
