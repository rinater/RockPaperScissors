# read animals.txt
file = open('animals.txt')
# and write animals_new.txt
file_new = open('animals_new.txt', '+a')
for name in file:
    file_new.write(name + '\n')
file.close()
file_new.close()
