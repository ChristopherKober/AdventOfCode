
part1_solution = 0
part2_solution = 0
data = []


with open('day6.txt', encoding='utf-8') as input:
    for line in input:
        data.append(line)

for j in data:
    total = 0
    words = j.split(" ")
    firstNums = list(map(int,words[-3].split(",")))
    secondNums = list(map(int,words[-1][:-1].split(",")))
    if secondNums[1] == 2410:
        print("\n\n")
        secondNums[1] = 241
    print(j,end="")
    total = (secondNums[0] - firstNums[0] + 1) * (secondNums[1] - firstNums[1] + 1)
    if words[0] == "toggle":
        total = 2*total
    elif words[1] == "off":
        total = -total
    part2_solution = part2_solution + total
                
    


            

print(part1_solution)
print(part2_solution)
