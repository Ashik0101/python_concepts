numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in range(len(numbers)):
#     if numbers[i] > 500:
#         break
#     if numbers[i] <= 150 and numbers[i] % 5 == 0:
#         print(numbers[i])


# using continue statement
for i in range(len(numbers)):
    if numbers[i] > 500:
        break
    if numbers[i] > 150:
        continue
    if numbers[i] % 5 == 0:
        print(numbers[i])
