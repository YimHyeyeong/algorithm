from sys import stdin

N, C = map(int, stdin.readline().split())
res = [0] * (C + 1)
cnt = 0

for _ in range(N):
    i = int(stdin.readline())
    for j in range(i, C+1, i):
        if res[j] == 0:
            res[j] = 1
            cnt += 1
print(cnt)