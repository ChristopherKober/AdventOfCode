part1_solution = 0


data = [[],[],[],[],[],[],[],[]]

people = ['Alice','Bob','Carol','David','Eric','Frank','George','Hallory','Ignacio']

with open('day13.txt') as input:
    for line in input:
        counter = ord(line[0]) - ord('A')
        if counter == len(data[ord(line[0]) - ord('A')]):
            data[ord(line[0]) - ord('A')] = data[ord(line[0]) - ord('A')] + [0]
        newData = line.split(' ')
        num = int(newData[3])
        if newData[2] == 'lose':
            num = -num
        data[ord(line[0]) - ord('A')] += [num]
data[7] = data[7] + [0]
for i in range(8):
    data[i] = data[i] + [0]
data = data + [[0,0,0,0,0,0,0,0]]

print(data)

def calc(s):
    counter = 0
    for i in range(8):
        first = ord(s[i][0]) - ord('A')
        second = ord(s[i+1][0]) - ord("A")
        counter = counter + data[first][second]
    counter = counter + data[ord(s[8][0]) - ord('A')][ord(s[0][0]) - ord('A')]

    for i in range(8,0,-1):
        first = ord(s[i][0]) - ord('A')
        second = ord(s[i-1][0]) - ord('A')
        counter = counter + data[first][second]
    counter = counter + data[ord(s[0][0]) - ord('A')][ord(s[8][0]) - ord('A')]

    return counter
    

seating = ['','','','','','','','']
temp = [0,1,2,3,4,5,6,7,8]
for a in range(9):
    for b in range(8):
        for c in range(7):
            for d in range(6):
                for e in range(5):
                    for f in range(4):
                        for g in range(3):
                            for l in range(2):
                                seating = ['','','','','','','','','']
                                innerTemp = []
                                for i in temp:
                                    innerTemp = innerTemp + [i]
                                h = [a,b,c,d,e,f,g,l,0]
                                for i in range(len(h)):
                                    seating[i] = innerTemp[h[i]]
                                    innerTemp.remove(innerTemp[h[i]])
                                for i in range(len(seating)):
                                    seating[i] = people[seating[i]]
                                part1_solution = max(part1_solution,calc(seating))

print(part1_solution)
                            
