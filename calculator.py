num1 = float(input("Enter the first number: "))
operator = input("Enter your operator here: ")
num2 = float(input("Enter your second number here: "))


if operator == "+":
    print(num1 + num2)

if operator == "-":
    print(num1 - num2)
if operator == "*":
    print(num1 * num2)
if operator == "/":
    print(num1 / num2)
if operator not in ("+", "-", "*", "/"):
    print("Invalid Operator.")


