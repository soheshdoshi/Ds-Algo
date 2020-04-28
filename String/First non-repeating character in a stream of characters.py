def mySolution(arr):
    mp = {}
    l = []
    s = ''
    for i in arr:
        if i not in mp:
            mp[i] = 1
            l.append(i)
        else:
            mp[i] = 0
        while l and mp[l[0]] == 0:
            l.pop(0)
        if not l:
            s += '#'
        else:
            s += l[0]
    return s


arr="abcabc"
print(mySolution(arr))
