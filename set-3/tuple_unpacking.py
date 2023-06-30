my_list = [("rohan", 22), ('sohan', 20), ('mohan', 22),
           ('ronan', 22), ('aslam', 22), ('sonam', 22), ('anam', 3)]


# for i in range(len(my_list)):
#     name, age = my_list[i]
#     print(f"{name} is {age} year old", end=". ")


# tuple unpacking directly
for name, age in my_list:
    print(f"{name} is {age} year old.", end=" ")
