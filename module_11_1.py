def introspection_info(obj):
    import inspect
    info = {}
    if inspect.isclass(obj):
        info['type'] = 'class'
    else:
        info['type'] = str(type(obj)).split("'")[1]
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['module'] = inspect.getmodule(obj)
    return info


class Sclass:
    attr1 = 42
    attr2 = 3.14
    attr3 = []

    def __init__(self):
        pass

    def ninja(self):
        pass

    def samurai(self):
        pass

    def ronin(self):
        pass


a = []


def function(x):
    return x ** 2


c = 42
func = function

print(introspection_info(Sclass))
print(introspection_info(a))
print(introspection_info(func))
print(introspection_info(c))
