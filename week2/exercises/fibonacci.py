"""
- newborn pair of rabbits (M, F) put in pen
- rabbits mate @ 1 month
- rabbits have 1 month gestation period
- assume rabbits never die, that females always produce 1 new pair (M, F) every month from their second month on
- how many female rabbits are there at the end of x months?
"""

def fib(x):
    """
    assumes x an int >=0
    returns Fibonacci of x
    """

    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
