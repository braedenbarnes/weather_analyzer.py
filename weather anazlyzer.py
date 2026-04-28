def load_data(filename):
    data = []
    with open(filename, "r") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(",")
            city = parts[0]
            country = parts[1]
            temp = parts[2]
            data.append((city, country, temp))
    return data


def display_data(data):
    for city, country, temp in data:
        print(f"{city}, {country}: {temp}")


def search_city(data, city_name):
    for city, country, temp in data:
        if city.lower() == city_name.lower():
            print(f"{city}: {temp}")
            return
    print("City not found")
    def add_city(filename):
    city = input("Enter city: ")
    country = input("Enter country: ")
    temp = input("Enter temperature: ")

    with open(filename, "a") as file:
        file.write(f"\n{city},{country},{temp}")

    print("City added!")


def main():
    filename = "weather.csv"
    data = load_data(filename)

    while True:
        print("\n1. View Data")
        print("2. Search City")
        print("3. Add City")
        print("4. Exit")

 choice = input("Choose an option: ")
if choice == "1":
    display_data(data)
 elif choice == "2":
     city = input("Enter city name: ")
            search_city(data, city)

