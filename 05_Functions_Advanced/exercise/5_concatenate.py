def concatenate(*args, **kwargs):
    result = ""

    for el in args:
        result += el

    for keys, values in kwargs.items():
        if keys in result:
            result = result.replace(keys, values)

    return result


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

