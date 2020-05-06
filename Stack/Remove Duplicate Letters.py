from collections import deque
def mySolution(s):
    result = ''
    while s:
        print(list(map(s.rindex, set(s))))
        i = min(map(s.rindex, set(s)))
        c = min(s[:i+1])
        result += c
        s = s[s.index(c):].replace(c, '')
    return result




a="cbacdcbc"
print(mySolution(a))