from functools import wraps

from connection import connection


def query(commited: bool = False, returns_data: bool = True, many: bool = True):
    def inner(function):
        @wraps(function)
        def wrapper(cls, *args, **kwargs):
            query_string = function(cls, *args, **kwargs)
            with connection.cursor() as cursor:
                cursor.execute(query_string)
                if commited:
                    connection.commit()
                if returns_data:
                    if many:
                        return [cls(country) for country in cursor.fetchall()]
                    return cls(cursor.fetchone())

        return wrapper

    return inner
