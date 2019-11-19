fileName = "data/digitdata/trainingimages"
# fp = open(fileName, 'r')
numbers = []
with open(fileName) as fp:
    line = fp.readline()
    countRows = 0
    while line:
        row = []
        for c in line:
            if c == ' ':
                row.append(0)
            else:
                row.append(1)
        row.pop(len(row) - 1)
        countRows += 1
        if countRows == 200:
            break
        numbers.append(row)
        line = fp.readline()

for n in numbers:
    print(n)
