# width = int(input())  # the number of cells on the X axis
# height = int(input())  # the number of cells on the Y axis
# L = []

# L = ['00','0.']  # 2x2
# L = ['0.0.0']  # horizontal
# L = ['0', '0', '0', '0']  # vertical
L = ['0.0', '...', '0.0']  # square
width = len(L[0])
height = len(L)

# for i in range(height):
# width characters, each either 0 is node or . is empty
# L.append(list(input()))

APU = [['' for r in range(height)] for c in range(width)]
for c in range(width):
    for r in range(height):
        APU[c][r] = L[r][c]


def find_rn(a, col, row, w):
    for i in range(col + 1, w):
        if a[i][row] == "0":
            return i, row
    return -1, -1


def find_bn(a, col, row, h):
    for i in range(row + 1, h):
        if a[col][i] == "0":
            return col, i
    return -1, -1


for r in range(height):
    for c in range(width):

        if APU[c][r] == "0":
            current_node = "{} {} ".format(c, r)
            rn = find_rn(APU, c, r, width)
            bn = find_bn(APU, c, r, height)

            print(current_node + "{} {}".format(rn[0], rn[1]) + " {} {}".format(bn[0], bn[1]))
