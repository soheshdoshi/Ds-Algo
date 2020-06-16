def mySolution(num):
    if len(num) == 0 or num is None:
        return 0

    def dfs(str):
        if len(str) > 0:
            if str[0] == '0':
                return 0
        if str == "" or len(str) == 1:
            return 1
        if int(str[:2]) <= 26:
            first = dfs(str[1:])
            second = dfs(str[2:])
            return first + second
        else:
            return dfs(str[1:])

    result = dfs(num)
    return result
