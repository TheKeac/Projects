import time # Adds a time delay so the user can read the output before returning to the menu

def calculator():
    # A basic calculator that performs various operations
    # such as addition, subtraction, multiplication, division, exponentiation,
    # modulus, floor division, square root, and percentage.
    while True:
        print("Welcome to the calculator!")
        print("Select an operation:")
        print("1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (*)")
        print("4: Division (/)")
        print("5: Exponentiation (^)")
        print("6: Modulus (%)")
        print("7: Floor Division (//)")
        print("8: Square Root (sqrt)")
        print("9: Percentage (%)")
        print("10: To exit the calculator")
        # Loops back to menu until user ends the loop with '10'

        choice = input("Enter the number of your choice (1/2/3/4/5/6/7/8/9/10): ")
        # Prompts user for their choice of operation

        if choice == '10':
            print("Thanks for using the calculator! Goodbye.")
            break  # Exits the loop

        while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print("Invalid choice! Please select a valid operation.")
            choice = input("Enter the number of your choice (1/2/3/4/5/6/7/8/9/10): ")
            
        num1, num2 = get_numbers()
        # Prompts user for two numbers to perform the operation on

        if choice == '1': # Addition
            print(f"The result is: {num1 + num2}")
            print("Returning to menu in 5 seconds...")
            time.sleep(5)
        elif choice == '2': # Subtraction
            print(f"The result is: {num1 - num2}")
            print("Returning to menu in 5 seconds...")
            time.sleep(5)
        elif choice == '3': # Multiplication
            print(f"The result is: {num1 * num2}")
            print("Returning to menu in 5 seconds...")
            time.sleep(5)
        elif choice == '4': # Division
            print(f"The result is: {(num1 / num2):.2f}")
            print("Returning to menu in 5 seconds...")
            time.sleep(5)
        elif choice == '5': # Exponentiation
            print(f"The result is: {num1 ** num2}")
            print("Returning to menu in 5 seconds...")
            time.sleep(5)
        elif choice == '6': # Modulus
            print(f"The result is: {num1 % num2}")
            print("Returning to menu in 5 seconds...")
            time.sleep(5)
        elif choice == '7': # Floor Division
            print(f"The result is: {num1 // num2}")
            print("Returning to menu in 5 seconds...")
            time.sleep(5)
        elif choice == '8': # Square Root
            if num1 >= 0:
                print(f"The result is: {num1 ** 0.5:.2f}")
                print("Returning to menu in 5 seconds...")
                time.sleep(5)
            else:
                print("Error! Cannot calculate square root of a negative number.")
                print("Returning to menu in 5 seconds...")
                time.sleep(5)
        elif choice == '9': # Percentage
            if num2 != 0:
                print(f"The result is: {(num1 / num2) * 100:.2f}%")
                print("Returning to menu in 5 seconds...")
                time.sleep(5)
            else:
                print("Error! Cannot calculate percentage with zero as the second number.")
                print("Returning to menu in 5 seconds...")
                time.sleep(5)
        else:
            print("Invalid choice! Please try again.")

def get_numbers():
    while True: #Loops until valid input is received
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2 #Returns the two numbers as floats
        except ValueError:
            print("Invalid input! Please enter numeric values.")

calculator()