import requests

API_URL = "https://api.frankfurter.app/latest"


def convert_currency(amount, from_currency, to_currency):
    params = {
        "amount": amount,
        "from": from_currency.upper(),
        "to": to_currency.upper()
    }

    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        print("Unable to fetch exchange rate.")
        return

    data = response.json()
    result = data["rates"][to_currency.upper()]

    print("\n========== CURRENCY CONVERTER ==========")
    print(f"{amount} {from_currency.upper()} = "
          f"{result:.2f} {to_currency.upper()}")


def main():
    print("===== CURRENCY CONVERTER =====")

    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g. USD): ")
        to_currency = input("To currency (e.g. INR): ")

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        convert_currency(
            amount,
            from_currency,
            to_currency
        )

    except ValueError:
        print("Please enter a valid amount.")


if __name__ == "__main__":
    main()
