import sys
def mySolution(M):
    r = len(M)
    c = len(M[0])
    x = [[0 for x in range(c)] for y in range(r)]
    # set energy requirement of bottom right cell
    x[r - 1][c - 1] = 1 - M[r - 1][c - 1] if M[r - 1][c - 1] < 0 else 1

    for row in range(r - 1, -1, -1):
        for col in range(c - 1, -1, -1):
            if not (row == r - 1 and col == c - 1):  # exclude bottom right cell
                to_down = x[row + 1][col] if row < r - 1 else sys.maxsize  # boundary conditions
                to_right = x[row][col + 1] if col < c - 1 else sys.maxsize
                x[row][col] = max(1, min(to_down, to_right) - M[row][col])

    return x[0][0]

A = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
print(mySolution(A))