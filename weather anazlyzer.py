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
