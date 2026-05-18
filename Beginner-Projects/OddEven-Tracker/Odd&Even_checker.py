red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

while True:
    try:
        num = int(input("Enter a Number:"))
        if num%2 == 0:
            print(green +"This is an Even Number: "+ str(num) + reset)
        else:
            print(green + "This is an odd number: " + str(num) + reset)
    except ValueError:
        print(red + "Invalid input. Please enter a valid number." + reset)

        choice = input("Do you want to check another number? (yes/no):")
        if choice == "no":
            print("Goodbye!")
            break 