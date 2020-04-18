def mySolution(bookings,n):
    ans = [0] * (n + 2)
    for book in bookings:
        ans[book[0]] += book[2]
        ans[book[1] + 1] -= book[2]
    cur = 0
    for i in range(1, n + 1):
        cur += ans[i]
        ans[i] = cur
    return ans[1:-1]
A = 6
B = [ [1, 2, 10],
      [2, 4, 20],
      [2, 6, 30]]
print(mySolution(B,A))