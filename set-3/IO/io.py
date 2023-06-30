# reading from a file
file_path = "./input.txt"
file = open(file_path, "r")
file_content = file.read()
file.close()
total_words = 0
list_of_words = file_content.split()
for i in list_of_words:
    total_words += 1
print(total_words)


# writing to a file
new_file_path = "./output.txt"
new_file = open(new_file_path, "w")
new_file.write(f"Total no of words in input.txt is : {total_words}\n")
new_file.write("This is the new line after writing words\n")
for i in range(100):
    new_file.write(f"This is written for the {i+3} time\n")
new_file.close()
