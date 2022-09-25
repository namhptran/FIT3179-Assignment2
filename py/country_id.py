from csv import DictReader

def get_country_ids(file_name):
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = DictReader(file)
        countries = {row['country_id']: row['country'] for row in reader}
        print(countries)

    with open('../data/country_id_mapping.csv', 'w', encoding='utf-8') as file:
        file.writelines(f"{country_id},{country}\n" for country_id, country in countries.items())


def aggregate_best_estimate():
    with open('../data/country_id_mapping.csv', 'r', newline='', encoding='utf-8') as id_file, \
         open('../data/GEDEvent_v22_1.csv', 'r', newline='', encoding='utf-8') as data_file, \
         open('../data/best_death_estimate.csv', 'w', encoding='utf-8') as out_file:

        id_reader = DictReader(id_file)
        data_reader = DictReader(data_file)

        countries = {row['country_id']: row['country_name'] for row in id_reader}

        totals = {country_id: 0 for country_id in countries}
        for row in data_reader:
            country_id = row['country_id']
            best = row['best']

            if country_id in totals:
                totals[country_id] += int(best)
            else:
                totals[country_id] = int(best)

        out_file.writelines("country_id,country_name,best\n")

        out_file.writelines(f"{country_id},{countries[country_id]},{totals[country_id]}\n" for country_id in countries)


if __name__ == "__main__":
    aggregate_best_estimate()
