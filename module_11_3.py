import sys
from pprint import pprint
import sys


class MyClass:
    """" Это мой класс """

    def __init__(self):
        atribut_1 = 777

    def my_method(self):
        pass


def introspection_info(obj):
    property_obj = {}
    property_obj['id'] = id(obj)
    property_obj['hash'] = hash(obj)
    property_obj['type'] = type(obj).__name__
    property_obj['doc'] = obj.__doc__
    property_obj['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    property_obj['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]

    try:
        property_obj['module'] = obj.__module__
        property_obj['mro'] = obj.__mro__  # наследование
    except:
        pass

    property_obj['get_ref'] = sys.getrefcount(obj)  # количество ссылок на объект
    property_obj['get_size'] = sys.getsizeof(obj)  # сколько байтов выделяется для хранения объекта

    return property_obj


number_info = introspection_info(MyClass)
# number_info = introspection_info(42)

pprint(number_info, sort_dicts=False)
