employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict = {}
for i in range(len(employees)):
    new_dict[employees[i]] = defaults
print(new_dict)

# expected ouput
# {
#     'Kelly':
#         {'designation': 'Developer', 'salary': 8000},
#     'Emma':
#         {'designation': 'Developer', 'salary': 8000}
# }
