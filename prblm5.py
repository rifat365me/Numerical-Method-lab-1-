a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter a operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    print("Result:", a / b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid operator")
