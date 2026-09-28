def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    amount = principal + interest

    return interest, amount


def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal

    return interest, amount


def main():
    print("========== INTEREST CALCULATOR ==========")
    print("1. Simple Interest")
    print("2. Compound Interest")

    choice = input("\nEnter your choice: ")

    try:
        principal = float(input("Enter principal amount: ₹"))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time (years): "))

        if principal <= 0 or rate < 0 or time <= 0:
            print("Please enter valid values.")
            return

        if choice == "1":
            interest, amount = simple_interest(
                principal, rate, time
            )

        elif choice == "2":
            interest, amount = compound_interest(
                principal, rate, time
            )

        else:
            print("Invalid choice.")
            return

        print("\n========== RESULT ==========")
        print(f"Principal: ₹{principal:.2f}")
        print(f"Interest:  ₹{interest:.2f}")
        print(f"Total Amount: ₹{amount:.2f}")

    except ValueError:
        print("Please enter numbers only.")


if __name__ == "__main__":
    main()
