def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fibef(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fibef(n-1, d) + fibef(n-2, d)
        d[n] = ans
        return ans


numFibCalls = 0
fibArg = #number here

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0

d = {1:1, 2:2}
print(fibef(fibArg, d))
print('function calls', numFibCalls)
