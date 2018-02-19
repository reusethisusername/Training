"""

The program:
Your program must judge results of marathon runners and choose the best one.
The result of each runner is represented as HH:MM:SS, where HH is hours, MM is minutes and SS is seconds.
You are given N results and the smallest time is the best.

Input
4
10:15:46
03:59:08
04:00:08
03:59:09

"""

from datetime import timedelta

n = int(input())
l = list()
for i in range(n):
    t = input()
    duration = timedelta(hours=int(t.split(":")[0]), minutes=int(t.split(":")[1]), seconds=int(t.split(":")[2]))
    l.append(duration)  # add duration to a list
print(str(min(l)).zfill(8))  # print min from the list, fill with leading 0s if hour is less than 10

# easiest solution
# print(min([input() for x in range(int(input()))]))
