# read sums.txt
file = open('sums.txt')
for line in file:
    summa = int(line.split()[0]) + int(line.split()[1])
    print(summa)
file.close()
