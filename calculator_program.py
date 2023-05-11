# Create a while function
while True:
    # Ask the user for the operation they want to use
    print("Which mathematical operation would you like to choose? ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION")
    operation = input("= ").upper()
    # Create if, elif, and else function for +
    if operation == "ADDITION":
        print("You chose addition!")
        try:
            number1 = input("What is your first number: ")
            number2 = input("What is your second number: ")
            sum = int(number1) + int(number2)
            print(sum)
        except ValueError:
            print("An error has occurred, please try again.")

# Ask for numbers and create a program for the operation
# Ask the user if they want to repeat the program from the beginning.
# Ask for numbers and create a program for the operation
# Ask the user if they want to repeat the program from the beginning.
# Create if, elif, and else function for -
# Ask for numbers and create a program for the operation
# Ask the user if they want to repeat the program from the beginning.
# Create if, elif, and else function for *
# Ask for numbers and create a program for the operation
# Ask the user if they want to repeat the program from the beginning.
# Create if, elif, and else function for /
# Ask for numbers and create a program for the operation
# Ask the user if they want to repeat the program from the beginning.
