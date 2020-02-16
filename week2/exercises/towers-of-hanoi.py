"""
The story:
- 3 tall spikes
- stack of 64 different sized discs - start on one spike
- need to move stack to second spike (at which point universe ends)
- can only move one disc at a time, & a larger disc cannot cover up a smaller one
"""

def printMove(fr, to):
    print(f'move from {fr} to {to}')

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
