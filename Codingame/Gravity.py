# grid = []
# width, height = [int(i) for i in input().split()]
# for i in range(height):
#     grid.append(list(input()))
#

# grid = {0: list('...#...#.#.#...#.'),
#         1: list('.#..#...#....#...'),
#         2: list('..........#......'),
#         3: list('..###...###..##..'),
#         4: list('#################')}
# width = len(grid.get(0))
# height = len(grid.keys())
grid = [list('...#...#.#.#...#.'),
        list('.#..#...#....#...'),
        list('..........#......'),
        list('..###...###..##..'),
        list('#################')]
width = len(grid[0])
height = len(grid)


def drop(h, v, g):
    j = height - 1  # search from bottom-up for a free space
    while j > h:  # watch out for anti-gravity
        if g[j][v] == '.':
            g[j][v] = '#'
            g[h][v] = '.'
            break
        else:
            j -= 1
    return g  # return updated grid


for r in range(height):
    for c in range(width):
        if grid[r][c] == '#':
            grid = drop(r, c, grid)

    print(''.join(grid[r]))
