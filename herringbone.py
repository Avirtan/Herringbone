array = [["-", "*", "-", "-", "-", "-", "-", "-", "-"],
         ["*", "-", "-", "-", "*", "-", "*", "-", "-"],
         ["-", "*", "-", "-", "*", "*", "*", "-", "*"],
         ["*", "*", "-", "*", "*", "*", "*", "-", "*"]]

underlineTotalCount = 4
for line in array:
    underlineCount = 0
    step = 0
    i = 0
    stopPosition = 0
    direction = 1
    while True:
        if line[i] == '-':
            indexReplace = i - step * direction
            tmp = line[i]
            line[i] = line[indexReplace]
            line[indexReplace] = tmp
            underlineCount += 1
            i = indexReplace
            step = 0

        if line[i] == '*':
            step += 1

        if direction == -1 and i == stopPosition:
            break
        i += 1 * direction

        if underlineCount == underlineTotalCount:
            stopPosition = i
            direction = -1
            i = len(line)-1
            underlineCount += 1
    underlineTotalCount -= 1
    print(line)
