import sys

# r_1 = int(input())
# r_1 = 20  # NO
# r_1 = 6 #YES
# r_1 = 80 #YES
# r_1 = 9915 #YES
r_1 = 42406  # NO
rivers = 0

for i in range(r_1 - 1, 1, -1):
    s = i
    s = s + sum([int(n) for n in str(s)])
    # print("i={},s={},r_1={}".format(i, s,r_1))
    if s == r_1:
        r_1 = i
        rivers += 1
        if rivers >= 2:
            print("YES")
            exit()
print("NO")
