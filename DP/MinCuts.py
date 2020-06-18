def minCut(self, s):
    cut = [x for x in range(-1, len(s))]
    for i in range(0, len(s)):
        forw = ''
        rev = ''
        for j in range(i, len(s)):
            forw += s[j]
            rev = s[j] + rev
            if forw == rev:
                cut[j + 1] = min(cut[j + 1], cut[i] + 1)
    return cut[-1]