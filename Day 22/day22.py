data = []

with open('day22.txt') as input:
    for line in input:
        data = data + [line]


a = 1
b = 0
line = 0
while True:
    if line >= 49:
        break
    temp = data[line]
    temp = temp.split(' ')
    if temp[0] == 'jio':
        if temp[1][0] == 'a':
            if a == 1:
                x = 1
                if temp[2][0] == '-':
                    x = -1
                y = int(temp[2][1:])
                line = line + y*x
                continue
        else:
            if b == 1:
                x = 1
                if temp[2][0] == '-':
                    x = -1
                y = int(temp[2][1:])
                line = line + y*x
                continue
    elif temp[0] == 'inc':
        if temp[1][0] == 'a':
            a = a + 1
        else:
            b = b + 1
    elif temp[0] == 'tpl':
        if temp[1][0] == 'a':
            a = a * 3
        else:
            b = b * 3
    elif temp[0] == 'jmp':
        x = 1
        if temp[1][0] == '-':
            x = -1
        y = int(temp[1][1:])
        line = line + x*y
        continue
    elif temp[0] == 'jie':
        if temp[1][0] == 'a':
            if a % 2 == 0:
                x = 1
                if temp[2][0] == '-':
                    x = -1
                y = int(temp[2][1:])
                line = line + x*y
                continue
        else:
            if b % 2 == 0:
                x = 1
                if temp[2][0] == '-':
                    x = -1
                y = int(temp[2][1:])
                line = line + x*y
                continue
    elif temp[0] == 'hlf':
        if temp[1][0] == 'a':
            a = a//2
        else:
            b = b//2
    line = line + 1

print(b)
