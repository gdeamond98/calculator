def add(a: float, b: float) -> float:
    """Return the sum of two numbers"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the subtraction of two numbers"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the multiplication of two numbers"""
    return a * b

def divide(a: float, b: float) -> float:
    """Return the division of two numbers"""
    return a / b

def read_number(prompt: str) -> float:
    """Read the users prompt and transform it into float """
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid number")

def main() -> None:
    while True:
        print("Operations available:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        operation = input("Select operation: ").strip()
        while operation not in ["1", "2", "3", "4", "5"]:
            print("Invalid input. Select a valid option.")
            operation = input("Select operation: ").strip()

        if operation == "5":
            print("Closing calculator... Bye")
            break

        num1 = read_number("Enter the first number: ")
        num2 = read_number("Enter the second number: ")

        if operation == "1":
            result = add(num1,num2)
        elif operation == "2":
            result = subtract(num1, num2)
        elif operation == "3":
            result = multiply(num1, num2)
        elif operation == "4":
            if num2 == 0:
                print("Zero Division Error.")
                continue
            else:
                result = divide(num1, num2)

        print(f"The result is {result}")

if __name__ == '__main__':
    main()




