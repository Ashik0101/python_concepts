def divide(a, b):
    try:
        division = a/b
        return division
    except ZeroDivisionError:
        return "Cannot divide a number with zero!"


print(divide(15, 10))
print(divide(100, 0))
