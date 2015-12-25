weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]

armor = [[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5],[0,0,0]]

rings = [[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]

#with open('day21.txt', encoding='utf-8') as input:
#    for line in input:
#        if not line == "":
#           data.append(line[:-1])

minCost = 1000000

for weap in weapons:
    for arm in armor:
        cost = weap[0] + arm[0]
        damage = weap[1] + arm[1]
        prot = weap[2] + arm[2]
        if (9 - prot) < (damage - 2) or (9 - prot) == (damage - 2) and (damage - 2) > 3:
            minCost = min(minCost,cost)

for weap in weapons:
    for arm in armor:
        for r in rings:
            cost = weap[0] + arm[0] + r[0]
            damage = weap[1] + arm[1] + r[0]
            prot = weap[2] + arm[2] + r[0]
            if (9 - prot) < (damage - 2) or (9 - prot) == (damage - 2) and (damage - 2) > 3:
                minCost = min(minCost,cost)
print(minCost)
