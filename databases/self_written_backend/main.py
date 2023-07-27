from queries import Country, insert_student

if __name__ == '__main__':
    print(Country.get_all_countries())
    ukraine = Country.get_country_by_id(9)
    print(ukraine)
    insert_student("Sashko", "Sobran", "M", ukraine)
