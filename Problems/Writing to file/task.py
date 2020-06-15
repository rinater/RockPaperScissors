f_name = "test.txt"
my_string = "A string to be written to a file!"

# what to do with the file and the string
file = open(f_name, 'w')
print("A string to be written to a file!", flush=True, file=file)
file.close()
