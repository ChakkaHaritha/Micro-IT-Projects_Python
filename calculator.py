# Simple Calculator in Python

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# If the choice is not valid, print an error and exit
if choice not in ['1', '2', '3', '4']:
    print("Invalid input. Exiting program. Please choose a valid operation next time.")
else:
    # If the choice is valid, ask for numbers
   
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        # Perform the selected operation
        if choice == '1':
            result = num1 + num2
            print(f"The result is: {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"The result is: {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"The result is: {result}")

        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is: {result}")
            else:
                print("Error: Cannot divide by zero.")
