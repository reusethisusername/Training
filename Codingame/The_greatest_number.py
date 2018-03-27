import itertools

n = 8
l = ['4', '9', '8', '.', '8', '5', '2', '-']
# l = ['9', '9', '8', '7', '5', '4', '2', '.', '1']
#l = ['0', '-', '0']
#l = ['1', '0', '0', '0', '0', '0', '.', '0']
# n = int(input())
# l = list(input().split())

if '-' in l:
    l.remove('-')
    perms = [''.join(x) for x in itertools.permutations(l, len(l))]
    b = [y for y in perms if y[0] != "."]
    g = '-{}'.format(min(b))
    try:
        if int(g) == float(g):
            print(int(g))
    except ValueError:
        print(g.rstrip('0'))

else:
    perms = [''.join(x) for x in itertools.permutations(l, len(l))]
    b = [y for y in perms if y[-1] != "."]
    g = max(b)
    try:
        if int(g) == float(g):
            print(int(g))
    except ValueError:
        print(g.rstrip('0') if g.rstrip('0')[-1]!='.' else print())
