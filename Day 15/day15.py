def calcVal(F,C,B,S):
    if 5*F + 8*C + 6*B + S != 500:
        return 0
    return max(4*F-B,0) * max(5*C-2*F,0) * max(5*B - 2*S - C,0) * max(2*S,0)

def main():
    part1_solution = 0
    for i in range(1,98):
        for j in range(1,98-i):
            for k in range(1,98-i-j):
                part1_solution = max(part1_solution,calcVal(i,j,k,100-i-j-k))
    print(part1_solution)
