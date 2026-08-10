# Simple calculator

try:
    # Taking input as string
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Type casting to float
    num1 = float(num1)
    num2 = float(num2)

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    # Handling division by zero
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus:", num1 % num2)
    print("Exponentiation:", num1 ** num2)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

except Exception as e:
    print("Unexpected error:", e)