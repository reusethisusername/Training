'''
Created on May 16, 2017

'''

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
L = []

for i in range(height):
    # width characters, each either 0 is node or . is empty
    L.append(list(input()))
APU = [['' for r in range(height)] for c in range(width)]
for c in range(width):
    for r in range(height):
        APU[c][r] = L[r][c]

for r in range(height):
    for c in range(width):
        if APU[c][r] == "0":
            break
            # check if it has right N
            # check if it has bottom N
            # print string

            # node, node to right, node to bottom

print(APU)
print(APU[0][1], '\n', end='')
print(APU[1][1], '\n', end='')

# Three coordinates: a node, its right neighbor, its bottom neighbor
#print("0 0 1 0 0 1")
