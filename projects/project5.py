# Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons
# that are “pushed,” and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process
# the basic arithmetic operations and a reset/clear operation.

def print_help():
    print("\nSimple Handheld Calculator")
    print("Commands:")
    print("  [number]       : Enter a number.")
    print("  +              : Add.")
    print("  -              : Subtract.")
    print("  *              : Multiply.")
    print("  /              : Divide.")
    print("  C              : Clear the screen.")
    print("  =              : Evaluate the expression.")
    print("  q              : Quit the calculator.")
    print()

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {e}"

def calculator():
    screen = ""
    print_help()
    
    while True:
        # Get user input
        user_input = input("Enter command: ").strip()
        
        if user_input.lower() == 'q':
            print("Quitting calculator.")
            break
        elif user_input.lower() == 'c':
            screen = ""
            print("Screen cleared.")
        elif user_input == '=':
            if screen:
                result = evaluate_expression(screen)
                print(f"Result: {result}")
                screen = str(result)  # Update screen with result
            else:
                print("Screen is empty. Enter an expression.")
        else:
            # Append input to the current screen expression
            screen += user_input
            print(f"Screen: {screen}")

if __name__ == "__main__":
    calculator()
