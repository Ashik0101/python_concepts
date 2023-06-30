ar = [2, 15, 11, 1007, 7]
tar = 9

for i in range(len(ar)-1):
    for j in range(i+1, len(ar)):
        if (ar[i] + ar[j]) == tar:
            print([i, j])


# Applied sorting
""" arr = [2, 15, 11, 7]
target = 9
arr.sort()
i = 0
j = len(arr)-1

while i < j:
    sum = arr[i] + arr[j]
    if sum > target:
        j -= 1
    elif sum < target:
        i += 1
    else:
        print([i, j])
        break """


# print(i, j)

# - *Output*: "[0, 1]"
