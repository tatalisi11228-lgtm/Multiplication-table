def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b

def ask_number(prompt):
    return float(input(prompt))


while True:
    print("1) Add   2) Subtract   3) Multiply   4) Divide   5) Quit")
    choice = input("Choice: ")
    if choice == "5":
        print("Exiting the calculator. Goodbye!")
        break
    elif choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue
    number1 = ask_number("Enter first number: ")
    number2 = ask_number("Enter second number: ")
    if choice == "1":
        result = add(number1, number2)
        print(f"({number1}) + ({number2}) = {result}")
    elif choice == "2":
        result = subtract(number1, number2)
        print(f"({number1}) - ({number2}) = {result}")
    elif choice == "3":
        result = multiply(number1, number2)
        print(f"({number1}) * ({number2}) = {result}")
    elif choice == "4":
        result = divide(number1, number2)
        if result is None:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"({number1}) / ({number2}) = {result}")
