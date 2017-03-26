while True:
    user_input = raw_input('Type quit to quit the program or choose =,-,*,**,%')
    if user_input=='quit':break

    elif user_input == '+' :
        #Addition
        print('Lets add 2 numbers')
        number1 = raw_input("Enter the first number: ")
        number2 = raw_input("Enter the second number: ")
        print('Your answer is: ')
        print int(number1) + int(number2)

    elif user_input == '-' :
        #Subtraction
        print('Lets subtract 2 numbers')
        number1 = raw_input("Enter the first number: ")
        number2 = raw_input("Enter the second number: ")
        print('Your answer is: ')
        print int(number1) - int(number2)

    elif user_input == '*' :
        #Multiplication
        print('Lets multiply 2 numbers')
        number1 = raw_input("Enter the first number: ")
        number2 = raw_input("Enter the second number: ")
        ('Your answer is: ')
        print int(number1) * int(number2)

    elif user_input == '/' :
        #Modulous
        print('Lets use division')
        number1 = raw_input("Enter the first number: ")
        number2 = raw_input("Enter the second number: ")
        print('Modulous is: ')
        print int(number1) / int(number2)
        
    elif user_input == '**' :
        #Exponent
        print('Lets use exponents')
        number1 = raw_input("Enter the first number: ")
        number2 = raw_input("Enter the second number: ")
        print('Your answer is: ')
        print int(number1) ** int(number2)

    elif user_input == '%' :
        #Modulous
        print('Lets use modulous')
        number1 = raw_input("Enter the first number: ")
        number2 = raw_input("Enter the second number: ")
        print('Modulous is: ')
        print int(number1) % int(number2)

zero = raw_input("Enter a number other than zero: ")
if zero == '0':
    print("You did not follow instructions you get a 0%.")
else:
    print("Awesome you get a 100%")
