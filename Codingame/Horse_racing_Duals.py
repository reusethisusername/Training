'''
Created on May 15, 2017
'''
# n = 3
# l = [5,8,9]

n = int(input())
l = list()

for i in range(n):
    pi = int(input())
    l.append(pi)

powers = sorted(l)
mn = powers[0]  # not working if powers[0]=0 should use sys.maxsize

for i in range(len(powers) - 1):
    if powers[i + 1] - powers[i] < mn:
        mn = powers[i + 1] - powers[i]

print(mn)
