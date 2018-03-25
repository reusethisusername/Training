'''
Created on May 16, 2017
'''

# width = int(input())  # the number of cells on the X axis
# height = int(input())  # the number of cells on the Y axis

# width = int(input())  # the number of cells on the X axis
# height = int(input())  # the number of cells on the Y axis
# L = []

# L = ['00','0.']  # 2x2
L = ['0.0.0']  # horizontal
#L = ['0', '0', '0', '0']  # vertical

width = len(L[0])
height = len(L)

# for i in range(height):
# width characters, each either 0 is node or . is empty
# L.append(list(input()))

APU = [['' for r in range(height)] for c in range(width)]
for c in range(width):
    for r in range(height):
        APU[c][r] = L[r][c]

for r in range(height):
    for c in range(width):
        s = "{} {} ".format(c, r)
        if APU[c][r] == "0":

            try:
                if APU[c + 1][r] == "0":  # check if it has right N
                    s = s + "{} {} ".format(c + 1, r)
                else:
                    s = s + "{} {} ".format(-1, -1)
            except IndexError:
                s = s + "{} {} ".format(-1, -1)
            try:
                if APU[c][r + 1] == "0":  # check if it has bottom N
                    s = s + "{} {} ".format(c, r + 1)
                else:
                    s = s + "{} {} ".format(-1, -1)
            except IndexError:
                s = s + "{} {} ".format(-1, -1)

            print(s.rstrip()) if len(s) > 10 else exit()

        elif APU[c][r] == ".":
            pass
        # node, node to right, node to bottom

# print(APU)
# print(APU[0][1], '\n', end='')
# print(APU[1][1], '\n', end='')

# Three coordinates: a node, its right neighbor, its bottom neighbor
# print("0 0 1 0 0 1")
