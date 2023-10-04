while True:
    print("Which lab would you like to run?")
    lab_number = input()

    # Build the filename based on the user's input
    filename = f"Lab{lab_number}.py"

    try:
        with open(filename) as f:
            code = f.read()
            exec(code)
        break  # Exit the loop if the input is valid and the file is executed
    except FileNotFoundError:
        print(f"Lab{lab_number}.py not found. Please enter a valid lab number.")
    except Exception as e:
        print(f"An error occurred: {e}")
