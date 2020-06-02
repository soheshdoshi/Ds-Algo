from heapq import heappush,heappop
def kthSmallestPrimeFraction(A, k):
    pq = []
    for i, v in enumerate(A):
        # Pushing [
        #	p/q (toCompare),
        #	rowNumber (To Prioritize Next Smallest Fraction)
        #   colNumber (To Prioritize Next Smallest Fraction)
        #   p (to retuen the value)
        #   q (to return the value) ]
        heappush(pq, (1 / v, i, 0, 1, v))

    while k > 0:
        # popping out the minimum
        v, row, col, p, q = heappop(pq)

        # if next value of same row is available
        if col < len(A):
            # if p < q then only push it to pq
            if row > col + 1:
                heappush(pq, (A[col + 1] / A[row], row, col + 1, A[col + 1], A[row]))
        k -= 1
    return [p, q]

A = [1, 2, 3, 5]
B = 3

print(kthSmallestPrimeFraction(A,B))