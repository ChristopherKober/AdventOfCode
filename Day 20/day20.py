target = 33100000


for i in range(775000,800000):
    curr = 0
    start = i//50
    temp = i//2+1
    for j in range(start,temp):
        if i%(j+1) == 0:
            curr = curr + (j+1)*11
    curr = curr + i*11
    if curr > target:
        print("Found:")
        print(i)
        break
    if i % 1000 == 0:
        print(i)
            
