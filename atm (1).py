# Predefined PIN and initial balance
PIN = "1234"
balance = 1000.0  # Initial balance

# Ask the user for their PIN
entered_pin = input("Enter your PIN: ")

# Check if the PIN is correct
if entered_pin == PIN:
    print("PIN correct. Welcome to your ATM.")

    while True:
        # Display menu options
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            # Check Balance
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == "2":
            # Withdraw Money
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > balance:
                print("Insufficient funds!")
            elif amount <= 0:
                print("Enter a valid amount.")
            else:
                balance -= amount
                print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")

        elif choice == "3":
            # Deposit Money
            amount = float(input("Enter the amount to deposit: $"))
            if amount <= 0:
                print("Enter a valid amount.")
            else:
                balance += amount
                print(f"Deposit successful! Your new balance is: ${balance:.2f}")

        elif choice == "4":
            # Exit
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

else:
    print("Incorrect PIN. Access denied!")
