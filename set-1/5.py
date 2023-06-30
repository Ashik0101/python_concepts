def reverse_string(string):
    reversed_str = ""
    for i in range(len(string)-1, -1, -1):
        reversed_str += string[i]
    return reversed_str


print(reverse_string("Python"))


# second way to reverse and the most efficient way
def rev_string(string):
    return string[::-1]


print(rev_string("ashikansari"))
