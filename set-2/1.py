# printe pattern
# for i in range(1, 6):
#     mylist = []
#     for j in range(i):
#         mylist.append(j+1)
#         str_list = [str(num) for num in mylist]
#     print(" ".join(str_list))

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
