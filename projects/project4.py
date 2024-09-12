#  Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.


def calculator():
    print("SIMPLE CALCULATOR")
    try:

        num= input("Enter the expression to solve: ")
        return eval(num)
    except:
        print("Invalid expression")
        return
    

cont='y'

while cont=='y':
    solution=calculator()
    print(solution)
    cont=input("Do you want to continue? (y/n): ")
    print('\n\n')