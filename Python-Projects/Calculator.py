def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def get_number():
    try:
        x = int(input("Enter First Number: "))
        y = int(input("Enter Second Number: "))
        return x, y
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return None, None


def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Calculator closed.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        x, y = get_number()
        if x is None:
            continue

        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", sub(x, y))
        elif choice == "3":
            print("Result:", mul(x, y))
        elif choice == "4":
            print("Result:", div(x, y))


calculator()
