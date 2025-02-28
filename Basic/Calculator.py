def calculator(a, b, operation):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return "Invalid operation"

# User input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Calculate
result = calculator(a, b, operation)
print(f"The result is {result}")
