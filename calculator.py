import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Get arguments
if len(sys.argv) == 4:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]
    
    if operation == "add":
        print(f"Result: {add(num1, num2)}")
    elif operation == "subtract":
        print(f"Result: {subtract(num1, num2)}")
    elif operation == "multiply":
        print(f"Result: {multiply(num1, num2)}")
    elif operation == "divide":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operation")
else:
    print("Invalid input. Usage: python calculator.py <num1> <num2> <operation>")
