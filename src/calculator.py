from src.utils import add, subtract, multiply, divide

def main():
    while True:
        print("\n=== Python Calculator ===")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

        choice = input("Choose operation: ")
        if choice == "5":
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
