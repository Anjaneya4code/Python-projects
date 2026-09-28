def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def main():
    print("========== TEMPERATURE CONVERTER ==========")
    print("1. Celsius → Fahrenheit")
    print("2. Celsius → Kelvin")
    print("3. Fahrenheit → Celsius")
    print("4. Fahrenheit → Kelvin")
    print("5. Kelvin → Celsius")
    print("6. Kelvin → Fahrenheit")

    choice = input("\nEnter your choice: ")

    try:
        temperature = float(input("Enter temperature: "))

        if choice == "1":
            result = celsius_to_fahrenheit(temperature)
            unit = "°F"

        elif choice == "2":
            result = celsius_to_kelvin(temperature)
            unit = "K"

        elif choice == "3":
            result = fahrenheit_to_celsius(temperature)
            unit = "°C"

        elif choice == "4":
            result = fahrenheit_to_kelvin(temperature)
            unit = "K"

        elif choice == "5":
            result = kelvin_to_celsius(temperature)
            unit = "°C"

        elif choice == "6":
            result = kelvin_to_fahrenheit(temperature)
            unit = "°F"

        else:
            print("Invalid choice.")
            return

        print("\n========== RESULT ==========")
        print(f"Converted Temperature: {result:.2f} {unit}")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
