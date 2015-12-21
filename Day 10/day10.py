import os

givenString = "1321131112"

infile = open("day10.txt","w")
infile.close()
os.remove("day10.txt")
infile = open("day10_temp.txt","w")
infile.close()
os.remove("day10_temp.txt")
infile = open("day10.txt","w")
infile.write(givenString)
infile.close()



for i in range(40):
    infile = open("day10.txt","r")
    outfile = open("day10_temp.txt","w")
    count = 1
    prev = ""
    curr = ""
    while True:
        nextChar = infile.read(1)
        if curr == "":
            prev = curr
            curr = nextChar
            continue
        if curr == nextChar:
            count = count + 1
        else:
            temp = str(count) + str(curr)
            outfile.write(temp)
            count = 1
        if nextChar == "":
            break
        prev = curr
        curr = nextChar
        
    infile.close()
    outfile.close()
    os.remove("day10.txt")
    secondinfile = open("day10_temp.txt","r")
    secondoutfile = open("day10.txt","w")
    while True:
        nextChar = secondinfile.read(1)
        if nextChar != "":
            secondoutfile.write(nextChar)
        else:
            break
    secondinfile.close()
    secondoutfile.close()
    os.remove("day10_temp.txt")


infile = open("day10.txt","r")
part1_solution = 0
while True:
    nextChar = infile.read(1)
    if nextChar == "":
        break
    part1_solution = part1_solution + 1
infile.close()

for i in range(10):
    infile = open("day10.txt","r")
    outfile = open("day10_temp.txt","w")
    count = 1
    prev = ""
    curr = ""
    while True:
        nextChar = infile.read(1)
        if curr == "":
            prev = curr
            curr = nextChar
            continue
        if curr == nextChar:
            count = count + 1
        else:
            temp = str(count) + str(curr)
            outfile.write(temp)
            count = 1
        if nextChar == "":
            break
        prev = curr
        curr = nextChar
        
    infile.close()
    outfile.close()
    os.remove("day10.txt")
    secondinfile = open("day10_temp.txt","r")
    secondoutfile = open("day10.txt","w")
    while True:
        nextChar = secondinfile.read(1)
        if nextChar != "":
            secondoutfile.write(nextChar)
        else:
            break
    secondinfile.close()
    secondoutfile.close()
    os.remove("day10_temp.txt")


infile = open("day10.txt","r")
part2_solution = 0
while True:
    nextChar = infile.read(1)
    if nextChar == "":
        break
    part2_solution = part2_solution + 1
infile.close()
    

print(part1_solution)
print(part2_solution)


