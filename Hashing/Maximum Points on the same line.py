from collections import Counter
def mySolution(A,B):
    points=list(zip(A,B))
    #print(points)
    answer = 0
    for p in points:
        pctr = 0
        ctr = Counter()
        for q in points:
            x, y = q[0] - p[0], q[1] - p[1]
            pctr += x == y == 0
            ctr[float(y)/x if x else 'inf'] += 1
        ctr['inf'] -= pctr
        answer = max(answer, pctr + max(ctr.values()))
    return answer


A = [-1, 0, 1, 2, 3, 3]
B = [1, 0, 1, 2, 3, 4]
print(mySolution(A,B))
