def add(dictionary, name, age):
    dictionary[name] = age
    return dictionary


def update(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age
    return dictionary


def delete(dictionary, name):
    if name in dictionary:
        del dictionary[name]
    return dictionary


dictionary = {}
print("After adding:", add(dictionary, "john", 24))
print("After updating:", update(dictionary, "john", 55))
print("After deleting:", delete(dictionary, "john"))
