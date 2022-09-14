from sys import stdin

N = int(stdin.readline())

cost = 0
for _ in range(N):
    lst = stdin.readline()
    lst = lst.replace(':', ' ')
    h, m, time = map(int, lst.split())

    if 7 <= h <= 18:
        if m + time >= 60 and h + 1 >= 19: # 요금이 바뀐다면
            t = m + time - 60
            cost += t * 5
            cost += (time - t) * 10
        else:
            cost += time * 10
    else:
        if m + time >= 60 and 7 <= h + 1 <= 18:
            t = m + time - 60
            cost += t * 10
            cost += (time - t) * 5
        else:
            cost += time * 5

print(cost)