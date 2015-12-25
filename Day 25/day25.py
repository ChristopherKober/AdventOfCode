start_row = 2947
start_col = 3029

row = start_row
col = start_col
while True:
    if col == 1:
        break
    row += 1
    col -= 1

counter = 0
for i in range(row):
    counter = counter + i

val = 20151125
for i in range(counter + start_col - 1):
    val = val * 252533
    val = val % 33554393

print("Part 1 Solution: ",end='')
print(val)
