def decodeAtIndex(S, K):
    def helper(stack, k, l):
        d = int(stack.pop())
        l //= int(d)
        if k % l == 0:
            k = l
        else:
            k %= l

        s = stack.pop()
        if l - len(s) < k <= l:
            return s[k - (l - len(s)) - 1]

        return helper(stack, k, l - len(s))
    l = 0
    start = -1
    stack = []
    for i in range(len(S)):
        if S[i].isdigit():
            s = S[start + 1: i]
            l += len(s)
            l *= int(S[i])
            stack.append(s)
            stack.append(S[i])

            if K <= l:
                return helper(stack, K, l)

            start = i
    return S[K - 1]

A="yc40gm70"
print(decodeAtIndex(A,107))