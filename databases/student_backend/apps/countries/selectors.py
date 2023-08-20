from apps.countries.models import Country


def get_all_countries():
    countries = Country.objects.all()
    return countries
