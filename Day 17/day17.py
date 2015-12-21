data = sorted([33,14,18,20,45,35,16,35,1,13,18,13,50,44,48,6,24,41,30,42])

counter = 0
for i in data:
    counter = counter + i
    if counter > 150:
        print(counter)
        print(i)
        break
