def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"


while True:
    num1 = int(input("Please enter first number: "))
    operator = input("Please enter operator (+, -, *, /): ")
    num2 = int(input("Please enter second number: "))

    result = calculate(num1, operator, num2)

    print(f"Result: {result}")

    again = input("Calculate again? y/n: ")

    if again == "n":
        break