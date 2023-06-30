s1 = "Aumlt"
s2 = "Kelly"


mid_index = len(s1) // 2
# print(s1[:mid_index]) => prints Au
# print(s1[mid_index:]) => prints mlt

print(s1[:mid_index] + s2 + s1[mid_index:])
