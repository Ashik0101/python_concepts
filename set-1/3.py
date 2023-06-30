
my_list = []

# adding 1 to 10 in list
for i in range(10):
    my_list.append(i+1)

print(my_list)


# adding another elements in the list using various methods.
my_list += [1]
my_list.append(12)
my_list.extend([2, 34, 200, 5, 6, 65])
print(my_list)


# deleting elements using various methods from list.
my_list.pop(-1)  # this will delete the element at last index.
del my_list[0]  # this will delete the element at 0th index
new_list = [x for x in my_list if x % 2 != 1]  # keep only desired element
print("new_list is : ", new_list)
print(my_list)


# sorting elements in the list
my_list.sort()
print("sorted in asc order  : ", my_list)

my_list.sort(reverse=True)
print("sorted in desc order  : ", my_list)

print()

# sort in asc order
nums = [12, 44, 55, 2, 4, 666, 2000]
sorted_nums = sorted(nums)
print("nums is :", nums)
print("sorted nums is :", sorted_nums)


# sort in desc order
sorted_nums = sorted(nums, reverse=True)
print("nums sorted in reversed :", sorted_nums)
