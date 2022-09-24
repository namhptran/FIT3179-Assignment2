from csv import DictReader

def read_file(file_name):
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = DictReader(file)
        countries = {row['country_id']: row['country'] for row in reader}
        print(countries)

    with open('../data/country_id_mapping.csv', 'w', encoding='utf-8') as file:
        file.writelines(f"{country_id},{country}\n" for country_id, country in countries.items())


if __name__ == "__main__":
    read_file("../data/GEDEvent_v22_1.csv")
