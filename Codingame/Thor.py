import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if
# Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position


def main():
    light_x, light_y, initial_tx, initial_ty = [
        int(i) for i in input().split()]
    xThor, yThor = initial_tx, initial_ty

# game loop
    while True:
        # The remaining amount of turns Thor can move. Do not remove this line.
        remaining_turns = int(input())

        goX = ""
        goY = ""

        if yThor > light_y:
            goY = "N"
            yThor = yThor - 1

        elif yThor < light_y:
            goY = "S"
            yThor = yThor + 1

        if xThor > light_x:
            goX = "W"
            xThor = xThor - 1

        elif xThor < light_x:
            goX = "E"
            xThor = xThor + 1

        print(goY + goX)


if __name__ == "__main__":
    main()
