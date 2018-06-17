# r_1 = int(input())
# r_2 = int(input())
r_1 = 32
r_2 = 47
# r1, r2 = [r_1], [r_2]

# v1 using lists
# while len(list(set(r1).intersection(r2))) != 1:
#     r1.append(int(r1[-1]) + sum([int(n) for n in str(r1[-1])]))
#     r2.append(int(r2[-1]) + sum([int(n) for n in str(r2[-1])]))
# print(list(set(r1).intersection(r2))[0])

# v2 using optimized lists
# if r_1 == r_2:
#     print(r_1)
# else:
#
#     while len(list(set(r1).intersection(r2))) != 1:
#         next_r1 = int(r1[-1]) + sum([int(n) for n in str(r1[-1])])
#         r1.append(next_r1)
#         if next_r1 < max(r1[-1], r2[-1]):
#             r1.remove(r1[0])
#         next_r2 = int(r2[-1]) + sum([int(n) for n in str(r2[-1])])
#         r2.append(next_r2)
#         if next_r2 < max(r1[-1], r2[-1]):
#             r2.remove(r2[0])
#     print(list(set(r1).intersection(r2))[0])

# v3 using loops
if r_1 == r_2:
    print(r_1)
else:
    a = min(r_1, r_2)
    b = max(r_1, r_2)
    while a != b:
        if a > b:
            b = b + sum([int(n) for n in str(b)])
        else:
            a = a + sum([int(n) for n in str(a)])
print(a)
