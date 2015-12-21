part1_solution = 0

infile = open('day12.txt','r')


hasANumber = False
number = 0
negative = 1
inStruct = False
stopCounting = False
structCount = 0
while True:
    curr = infile.read(1)
    if curr == '':
        break
    if curr == '{':
        inStruct = True
        structCount = 0
        stopCounting = False
    if curr == '}':
        inStruct = False
        if not stopCounting:
            part1_solution = part1_solution + structCount
    if curr == '-':
        negative = -1
    if curr == 'r':
        stopCounting = True
    if ord('0') <= ord(curr) and ord('9') >= ord(curr):
        if hasANumber:
            number = number * 10 + int(curr)
        else:
            number = int(curr)
            hasANumber = True
    elif hasANumber:
        hasANumber = False
        if not inStruct:
            part1_solution = part1_solution + number * negative
        elif inStruct:
            structCount = structCount + number * negative
        negative = 1
        number = 0

print(part1_solution)
        
