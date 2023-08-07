from functools import wraps

from connection import connection


def query(commited: bool = False, returns_data: bool = True, many: bool = True):
    def inner(function):
        @wraps(function)
        def wrapper(manager, *args, **kwargs):
            query_string = function(manager, *args, **kwargs)
            related_model = manager.related_model
            print(query_string)
            with connection.cursor() as cursor:
                cursor.execute(query_string)
                if commited:
                    connection.commit()
                if returns_data:
                    if many:
                        return [related_model(entity) for entity in cursor.fetchall()]
                    return related_model(cursor.fetchone())

        return wrapper

    return inner
