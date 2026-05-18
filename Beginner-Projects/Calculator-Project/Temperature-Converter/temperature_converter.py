red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

def celsius_to_farenheit(celsius):
    farenheit = (celsius*9/5) + 32
    return farenheit
def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius 

while True:
    print("1. Celsius to Farenheit")
    print("2. Farenheit to Celsius")
    print("3. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius"))
            farenheit = round(celsius_to_farenheit(celsius),2)
            print( green +f"{celsius} °C is equal to {farenheit} °F" + reset)
        except ValueError:
            print(red+"Invalid input. Please enter a valid number" + reset)

    elif choice == "2":
        try:
            farenheit = float(input("Enter temperature in Farenheit"))
            celsius = round(farenheit_to_celsius(farenheit),2)
            print(green +f"{farenheit} °F is equal to {celsius}°C"+ reset)
        except ValueError:
            print(red+"Invalid input. Please enter a valid number" + reset)
    elif choice == "3":
        print("Existing the program...")
        break 
    else:
        print(red+"Invalid choice. Please enter 1,2,3 only" + reset)
