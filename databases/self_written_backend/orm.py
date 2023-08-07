from decorators import query


class Manager:
    table_name: str
    related_model: type["Model"]

    def __init__(self, related_model):
        cls = self.__class__
        setattr(cls, "related_model", related_model)
        setattr(cls, "table_name", related_model.table_name)

    @staticmethod
    def get_query_specifications(items, separator: str):
        return separator.join([f"{arg}={repr(value)}" for arg, value in items])

    @classmethod
    @query(commited=True, returns_data=False)
    def create(cls, **kwargs):
        fields = kwargs.keys()
        field_values = [repr(value) for value in kwargs.values()]
        return f"INSERT INTO public.{cls.table_name} ({', '.join(fields)}) VALUES ({', '.join(field_values)});"

    @classmethod
    @query()
    def all(cls):
        return f"SELECT * FROM public.{cls.table_name}"

    @classmethod
    @query()
    def filter(cls, **kwargs):
        query_specification = cls.get_query_specifications(kwargs.items(), " AND ")
        return f"SELECT * FROM public.{cls.table_name} WHERE {query_specification};"

    @classmethod
    @query(many=False)
    def get(cls, **kwargs):
        query_specification = cls.get_query_specifications(kwargs.items(), " AND ")
        return f"SELECT * FROM public.{cls.table_name} WHERE {query_specification};"

    @classmethod
    @query(commited=True, returns_data=False)
    def update(cls, update_by: dict, **kwargs):
        updated_query = cls.get_query_specifications(update_by.items(), " AND ")
        query_specification = cls.get_query_specifications(kwargs.items(), ", ")
        return f"UPDATE public.{cls.table_name} SET {query_specification} WHERE {updated_query};"

    @classmethod
    @query(commited=True, returns_data=False)
    def delete(cls, **kwargs):
        query_specification = cls.get_query_specifications(kwargs.items(), " AND ")
        return f"DELETE FROM public.{cls.table_name} WHERE {query_specification};"


class Model:
    table_name: str
    id: int

    def __init__(self, object_id: int):
        self.id = object_id

    def update(self, **kwargs):
        return self.objects().update(update_by={"id": self.id}, **kwargs)

    def delete(self):
        return self.objects().delete(id=self.id)

    @classmethod
    def objects(cls):
        return Manager(cls)
