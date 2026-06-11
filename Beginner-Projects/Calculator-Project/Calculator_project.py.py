red = "\033[91m"  
green  = "\033[92m"
reset = "\033[0m"
while True: 
    num1=float(input("enter a number:"))
    num2=float(input("enter another number:"))
    op=input("enter an operator(+,-,*,/):")
    if op=="+":
        result=num1+num2
        print("you entered",num1,op,num2)
        print(green + "Result =" + str(result) + reset )
    elif op=="-":
        result=num1-num2
        print("you entered",num1,op,num2)
        print(green + "Result =" + str(result) + reset )
    elif op=="*":
        result=num1*num2
        print("you entered",num1,op,num2)
        print(green + "Result =" + str(result) + reset )
    elif op=="/":
        if num2==0:
            print(red + "Error! number cannot be divided by 0" + reset)
        else:
            result=num1/num2
            print("you entered",num1,op,num2)
            print(green + "Result =" + str(result) + reset )
    else:
        print("you entered",num1,op,num2)
        print(red + "Error! invalid operator" + reset)

    choice = input("Do you want to calculate again? (yes/no):")
    if choice == "no":
        print("Goodbye!")
        break
