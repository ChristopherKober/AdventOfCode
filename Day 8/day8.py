part1_solution = 0
part2_solution = 0

total_len = 0
char_len = 0

len2 = 0

data = []


with open('day8.txt', encoding='utf-8') as input:
    for line in input:
        if not line == "":
            data.append(line[:-1])



for i in data:
    total_len = total_len + len(i)
    char_len = char_len - 2
    inEscape = False
    num = 0
    for j in i:
        if inEscape:
            if j == "\\" or j == '"':
                inEscape = False
            elif j == "x":
                num = 0
            elif num == 0:
                num = num + 1
            elif num == 1:
                inEscape = False
        elif j == "\\":
            inEscape = True
            char_len = char_len + 1
        
        else:
            char_len = char_len + 1


for i in data:
    len2 = len2 + 2
    for j in i:
        if j == '"' or j == '\\':
            len2 = len2 + 2
        else:
            len2 = len2 + 1
            


part1_solution = total_len - char_len
part2_solution = len2 - total_len
print(part1_solution)
print(part2_solution)
