weights = [1,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]

goal = 389

piles = []

part1_solution = 999999988888888


for a in weights:
    for b in weights:
        for c in weights:
            for d in weights:
                for e in weights:
                    if a in [b,c,d,e] or b in [a,c,d,e] or c in [a,b,d,e] or d in [a,b,c,e] or e in [a,b,c,d]:
                        continue
                    if a*b*c*d*e == 77757221:
                        print([a,b,c,d,e])
                        continue
                    if (a + b + c + d + e) == goal:
                        part1_solution = min(part1_solution,a*b*c*d*e)

print(part1_solution)
    
    
        
