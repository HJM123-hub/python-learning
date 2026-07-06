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


def save_history(history):
    with open("history.txt", "w", encoding="utf-8") as file:
        for item in history:
            file.write(item + "\n")


def load_history():
    history = []

    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            for line in file:
                history.append(line.strip())

    except FileNotFoundError:
        pass

    return history


def show_history(history):
    if len(history) == 0:
        print("No history.")
    else:
        print("Calculation history:")
        for item in history:
            print(item)


def show_menu():
    print("====== Calculator Menu ======")
    print("1. Calculate")
    print("2. Show history")
    print("3. Clear history")
    print("4. Exit")
    print("=============================")


history = load_history()

while True:
    show_menu()
    choice = input("Please choose: ")

    if choice == "1":
        try:
            num1 = int(input("Please enter first number: "))
            operator = input("Please enter operator (+, -, *, /): ").strip()
            num2 = int(input("Please enter second number: "))

            result = calculate(num1, operator, num2)

            print(f"Result: {result}")

            record = f"{num1} {operator} {num2} = {result}"
            history.append(record)

        except ValueError:
            print("Invalid number. Please enter integers only.")

    elif choice == "2":
        show_history(history)

    elif choice == "3":
        history = []
        print("History cleared.")

    elif choice == "4":
        save_history(history)
        print("History saved to history.txt")
        break

    else:
        print("Invalid choice.")
