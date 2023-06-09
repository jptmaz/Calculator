# Create a while function
while True:
    # Ask the user for the operation they want to use
    print("Which mathematical operation would you like to choose? ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION")
    operation = input("= ").upper()
    
    # Create if, elif, and else function for +
    if operation == "ADDITION":
        print("You chose addition!")
        try:
              # Ask for numbers and create a program for the operation
            number1 = input("What is your first number: ")
            number2 = input("What is your second number: ")
            sum = int(number1) + int(number2)
            print(sum)
        except ValueError:
            print("An error has occurred, please try again.")

        # Ask the user if they want to repeat the program from the beginning.
        print("Would you like to try again?")
        Try_again = input("= ").upper()
        if Try_again == "YES":
            True
        elif Try_again == "NO":
            break

     # Create if, elif, and else function for -
    elif operation == "SUBTRACTION":
        print("You chose subtraction!")
        # Ask for numbers and create a program for the operation
        try:
            number1 = input("What is your first number: ")
            number2 = input("What is your second number: ")
            difference = int(number1) - int(number2)
            print(difference)
        except ValueError:
            print("An error has occurred, please try again.")

         # Ask the user if they want to repeat the program from the beginning.
        print("Would you like to try again?")
        Try_again = input("= ").upper()
        if Try_again == "YES":
            True
        elif Try_again == "NO":
            break

     # Create if, elif, and else function for *
    elif operation == "MULTIPLICATION":
        print("You chose multiplication!")
        # Ask for numbers and create a program for the operation
        try:
            number1 = input("What is your first number: ")
            number2 = input("What is your second number: ")
            product = int(number1) * int(number2)
            print(product)
        except ValueError:
            print("An error has occurred, please try again.")

         # Ask the user if they want to repeat the program from the beginning.
        print("Would you like to try again?")
        Try_again = input("= ").upper()
        if Try_again == "YES":
            True
        elif Try_again == "NO":
            break

    elif operation == "DIVISION":
        print("You chose division!")
        # Ask for numbers and create a program for the operation
        try:
            number1 = input("What is your first number: ")
            number2 = input("What is your second number: ")
            quotient = int(number1) / int(number2)
            print(quotient)
        except ValueError:
            print("An error has occurred, please try again.")

         # Ask the user if they want to repeat the program from the beginning.
        print("Would you like to try again?")
        Try_again = input("= ").upper()
        if Try_again == "YES":
            True
        elif Try_again == "NO":
            break
    # Create Else statement
    else:
        print("I do not understand the command, please input it once more.")
        print("Would you like to try again?")
        Try_again = input("= ").upper()
        if Try_again == "YES":
            True
        elif Try_again == "NO":
            break

# Thank the user
print("Thank you!")