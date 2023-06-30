# count no of vowels present in a string

string = "Hellojee"
vowels = 0
for i in range(len(string)):
    if string[i] == "a" or string[i] == "i" or string[i] == "e" or string[i] == "o" or string[i] == "u":
        vowels += 1
print("Number of vowels: ", vowels)
