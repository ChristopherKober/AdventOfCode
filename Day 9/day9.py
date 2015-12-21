data = []
cities = {}


with open('day9.txt', encoding='utf-8') as input:
    for line in input:
        if not line == "":
            data.append(line[:-1])


for i in data:
    j = i.split(" ")
    if not j[0] in cities:
        cities[j[0]] = len(cities)
    if not j[2] in cities:
        cities[j[2]] = len(cities)

for i in data:
    j = i.split(" ")
    print("(set-edge! day9",end = " ")
    print(cities[j[0]],end=" ")
    #print(j[1],end = " ")
    print(cities[j[2]],end = " ")
    #print(j[3],end = " ")
    print(j[4], end = "")
    print(')')

