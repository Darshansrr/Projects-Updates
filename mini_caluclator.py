print("=" * 40)
print("       🧮 MINI SMART CALCULATOR")
print("=" * 40)

print("1. Addition       (+)")
print("2. Subtraction    (-)")
print("3. Multiplication (*)")
print("4. Division       (/)")
print("5. Percentage     (%)")
print("6. Exit")

print("-" * 40)

choice = input("Enter your choice: ")

if choice == "6":
    print("\n👋 Thank you for using Calculator!")

elif choice in ["1", "2", "3", "4", "5"]:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        print("\n✅ Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("\n✅ Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("\n✅ Result:", result)

    elif choice == "4":
        if num2 == 0:
            print("\n❌ Cannot divide by zero!")
        else:
            result = num1 / num2
            print("\n✅ Result:", result)

    elif choice == "5":
        result = (num1 * num2) / 100
        print("\n✅ Result:", result)

else:
    print("\n❌ Invalid choice!")

print("=" * 40)