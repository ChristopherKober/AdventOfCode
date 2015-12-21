
part1_solution = 0
part2_solution = 0
data = []

vowels = ["a","e","i","o","u"]
naughty = ["ab","cd","pq","xy"]


with open('day5.txt', encoding='utf-8') as input:
    for line in input:
        data.append(line)


for i in data:
    vowelNum = 0
    double = False
    prevLetter = ""
    hasRestrictedStrings = False
    for j in i:
        if j in vowels:
            vowelNum = vowelNum + 1
        if j == prevLetter:
            double = True
        if prevLetter + j in naughty:
            hasRestrictedStrings = True
        prevLetter = j
    if (vowelNum > 2) and (double) and (not hasRestrictedStrings):
        part1_solution = part1_solution + 1








for i in data:
    doublePairs = []
    hasDoublePair = False
    oneLetterRepeat = False
    prevLetter = ""
    prevPrevLetter = ""
    for j in i:
        if not (prevLetter == ""):
            doublePairs = doublePairs + [prevLetter + j]
        if prevLetter + j in doublePairs[0:-2]:
            hasDoublePair = True
        if j == prevPrevLetter:
            oneLetterRepeat = True
        prevPrevLetter = prevLetter
        prevLetter = j
    if hasDoublePair and oneLetterRepeat:
        part2_solution = part2_solution + 1
            

print(part1_solution)
print(part2_solution)
