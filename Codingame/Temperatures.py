'''
Created on Nov 28, 2016
'''

import sys
import math


def main():

    # Auto-generated code below aims at helping you parse
    # the standard input according to the problem statement.

    n = int(input())  # the number of temperatures to analyse
    # the n temperatures expressed as integers ranging from -273 to 5526
    temps = input()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    posT = [5527]
    negT = [-274]

    newT = temps.split()
    if len(newT) == 1:
        for t in newT:
            print(int(t))
    else:
        for t in newT:
            if int(t) > 0:
                posT.append(int(t))
            elif int(t) < 0:
                negT.append(int(t))

        # print(posT)
        # print(negT)

        minP = min(posT)
        maxN = max(negT)

        if n == 0:
            print(n)
        elif minP <= abs(maxN):
            print(minP)
        elif minP > abs(maxN):
            print(maxN)

if __name__ == '__main__':
    main()
