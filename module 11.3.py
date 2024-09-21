import inspect


def introspection_info(obj):
    return {'type': type(obj).__name__, 'attributes': [i for i in dir(obj) if not callable(getattr(obj, i))], 'method': dir(obj), 'module': inspect.getmodule(introspection_info), 'Function?': inspect.isfunction(introspection_info)}
    # Верните словарь или строки с данными об объекте




number_info = introspection_info(42)

print(number_info)
