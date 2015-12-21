
data = {}


with open('day14.txt') as input:
    for line in input:
        temp = line.split(" ")
        data[temp[0]] = [int(temp[3]),int(temp[6]),int(temp[-2])]

def allDistances(time):
    ret = {}
    for keys in data:
        ret[keys] = 0
    for i in range(time):
        for keys in data:
            if i % (data[keys][1] + data[keys][2]) < data[keys][1]:
                ret[keys] = ret[keys] + data[keys][0]
    return ret

def maxDistance(time):
    temp = allDistances(time)
    retVal = 0
    for keys in temp:
        retVal = max(retVal,temp[keys])
    return retVal

def currWinner(time):
    temp = allDistances(time)
    winner = 'Rudolph'
    for keys in data:
        if temp[keys] > temp[winner]:
            winner = keys
    return winner

def allPoints(time):
    temp = {}
    for keys in data:
        temp[keys] = 0
    for i in range(time):
        winner = currWinner(i+1)
        temp[winner] = temp[winner] + 1
    return temp

def maxPoints(time):
    temp = allPoints(time)
    retVal = 0
    for keys in temp:
        if temp[keys] > retVal:
            retVal = temp[keys]
    return retVal

def main():
    part1_solution = maxDistance(2503)
    print(part1_solution)
    part2_solution = maxPoints(2503)
    print(part2_solution)

main()
        
        
