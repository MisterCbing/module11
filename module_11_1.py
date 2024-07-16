import math
def introspection_info(obj):
    import inspect
    info = {}
    info['type'] = str(type(obj)).split("'")[1]
    info['module'] = inspect.getmodule(obj)
    print(inspect.getmodule(obj))
    # for i in dir(obj):
    #     attr = getattr(obj, i)
    #     print(i, type(attr)))

    return info
a = []
def function(x):
    return x**2

c = 42
func = function

print(introspection_info(math.pi))
