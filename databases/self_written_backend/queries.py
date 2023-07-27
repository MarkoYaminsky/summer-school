from connection import connection
from decorators import query


class Country:
    id: int
    name: str

    def __init__(self, country_data: tuple[int, str]):
        self.id, self.name = country_data

    @classmethod
    @query(commited=True, returns_data=False)
    def insert_country(cls, country_name: str):
        return f"INSERT INTO public.country (name) VALUES ('{country_name}');"

    @classmethod
    @query()
    def get_all_countries(cls):
        return "SELECT * FROM public.country;"

    @classmethod
    @query(many=False)
    def get_country_by_name(cls, country_name: str):
        return f"SELECT * FROM public.country WHERE country.name='{country_name}';"

    @classmethod
    @query(many=False)
    def get_country_by_id(cls, country_id: int):
        return f"SELECT * FROM public.country WHERE country.id={country_id};"

    @classmethod
    @query(commited=True, returns_data=False)
    def update_country_by_id(cls, country_id: int, new_name: str):
        return f"UPDATE country SET name='{new_name}' WHERE id={country_id};"

    @classmethod
    @query(commited=True, returns_data=False)
    def delete_country_by_id(cls, country_id: int):
        return f"DELETE FROM country WHERE id={country_id};"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Country({self.id}, {repr(self.name)})"


def insert_student(first_name: str, last_name: str, sex: str, country: Country):
    query_string = f"INSERT INTO student (first_name, last_name, sex, country_id) " \
                   f"VALUES ('{first_name}', '{last_name}', '{sex}', {country.id});"

    cursor = connection.cursor()
    cursor.execute(query_string)
    connection.commit()
    cursor.close()
