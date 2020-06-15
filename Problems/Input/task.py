# write the code here
line = input()
file = open('input.txt', '+a')
file.write(line)
file.close()
