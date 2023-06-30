list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
rev = list(reversed(list2))

for i in range(len(list1)):
    print(list1[i], rev[i])
"""
10 400
20 300
30 200
40 100
"""
