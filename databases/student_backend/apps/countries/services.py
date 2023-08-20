from apps.countries.models import Country


def create_country(country_data: dict):
    # {"name": "Маленький принц", "author": "Екзюпері"}
    country = Country.objects.create(**country_data)  # ...create(name="Маленький принц", author="Екзюпері")
    return country


def update_country(country: Country, country_dict: dict):
    for key, value in country_dict.items():
        setattr(country, key, value)
    country.save()
    return country


def delete_country(country: Country):
    country.delete()
