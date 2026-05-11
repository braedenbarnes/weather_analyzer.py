import os

def load_data(filename):
    data = []

    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return data

    with open(filename, "r") as file:
        lines = file.readlines()

        if len(lines) == 0:
            print("Weather file is empty.")
            return data

        for line in lines[1:]:
            parts = line.strip().split(",")

            if len(parts) >= 3:
                city = parts[0]
                country = parts[1]
                temp = parts[2]

                data.append((city, country, temp))

    return data


def display_data(data):
    if len(data) == 0:
        print("No weather data available.")
        return

    print("\n===== Weather Data =====")

    for city, country, temp in data:
        print(f"{city}, {country}: {temp}°C")


def search_city(data, city_name):
    found = False

    for city, country, temp in data:
        if city.lower() == city_name.lower():
            print(f"\n{city}, {country}: {temp}°C")
            found = True
            break

    if not found:
        print("City not found.")


def add_city(filename):
    city = input("Enter city: ")
    country = input("Enter country: ")
    temp = input("Enter temperature: ")

    with open(filename, "a") as file:
        file.write(f"\n{city},{country},{temp}")

    print("City added successfully!")


def main():
    filename = "weather.csv"

    while True:
        data = load_data(filename)

        print("\n===== Weather File Analyzer =====")
        print("1. View Weather Data")
        print("2. Search for a City")
        print("3. Add New City")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_data(data)

        elif choice == "2":
            city_name = input("Enter city name: ")
            search_city(data, city_name)

        elif choice == "3":
            add_city(filename)

        elif choice == "4":
            print("Exiting Weather File Analyzer...")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


main()
