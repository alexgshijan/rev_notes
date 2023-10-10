def adding(number_one, number_two):
    numbers = int(number_one) + int(number_two)
    return numbers

def subtraction(number_one, number_two):
    numbers = int(number_one) - int(number_two)
    return numbers

def division(number_one, number_two):
    numbers = int(number_one) / int(number_two)
    return numbers

def multiplication(number_one, number_two):
    numbers = int(number_one) * int(number_two)
    return numbers

while True:
    choice = int(input("\nEnter operators : \n 1 for Multiply \n 2 for Divide \n 3 for Addition \n 4 for Subtraction\n"))

    if choice == 1:
        print(multiplication((input('Enter Number One : ')),(input('Enter Number Two : '))))
    elif choice == 2:
        print(division((input('Enter Number One : ')),(input('Enter Number Two : '))))
    elif choice == 3:
        print(adding((input('Enter Number One : ')),(input('Enter Number Two : '))))
    elif choice == 4:
        print(subtraction((input('Enter Number One : ')),(input('Enter Number Two : '))))
    else:
        print('IDEK what happened')

