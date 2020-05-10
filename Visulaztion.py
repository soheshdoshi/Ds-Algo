from functools import wraps
import builtins

def printRecursionTree(func):
    global _recursiondepth
    _print = builtins.print
    _recursiondepth = 0

    def getpads():
        if _recursiondepth == 0:
            strFn    = '{} └──'.format(' │  ' * (_recursiondepth-1))
            strOther = '{}  ▒▒'.format(' │  ' * (_recursiondepth-1))
            strRet   = '{}    '.format(' │  ' * (_recursiondepth-1))
        else:
            strFn    = '    {} ├──'.format(' │  ' * (_recursiondepth-1))
            strOther = '    {} │▒▒'.format(' │  ' * (_recursiondepth-1))
            strRet   = '    {} │  '.format(' │  ' * (_recursiondepth-1))

        return strFn, strRet, strOther

    def indentedprint():
        @wraps(builtins.print)
        def wrapper(*args, **kwargs):
            strFn, strRet, strOther = getpads()
            _print(strOther, end=' ')
            _print(*args, **kwargs)
        return wrapper


    @wraps(func)
    def wrapper(*args, **kwargs):
        global _recursiondepth

        strFn, strRet, strOther = getpads()

        if args and kwargs:
            _print(strFn, '{}({}, {}):'.format(func.__qualname__, ', '.join(args), kwargs))
        else:
            _print(strFn, '{}({}):'.format(func.__qualname__, ', '.join(map(str, args)) if args else '', kwargs if kwargs else ''))


        _recursiondepth += 1
        builtins.print, backup = indentedprint(), builtins.print

        retval = func(*args, **kwargs)

        builtins.print = backup
        _recursiondepth -= 1


        _print(strRet, '╰', retval)
        if _recursiondepth == 0:
            _print()
        return retval

    return wrapper

if __name__ == '__main__':
    @printRecursionTree
    def fib(n):
        if n <= 1:
            print('Base Case')
            return n
        print('Recursive Case')
        return fib(n-1) + fib(n-2)

    # This works with mutually recursive functions too,
    # since the variable _recursiondepth is global
    @printRecursionTree
    def iseven(n):
        print('checking if even')
        print('Note how the print')
        print('statements get nicely indented')
        if n == 0: return True
        return isodd(n-1)

    @printRecursionTree
    def isodd(n):
        print('checking if odd')
        if n == 0: return False
        return iseven(n-1)
    fib(5)