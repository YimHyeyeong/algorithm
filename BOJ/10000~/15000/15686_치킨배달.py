from sys import stdin
from itertools import combinations

N, M = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]

home = []  # 집 위치 저장
chicken = [] # 치킨집 위치 저장

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))

res = 21e8
for k in combinations(chicken, M):
    t = 0
    for q in home:
        cnt = 21e8
        for w in k:
            distance = abs(q[0]-w[0]) + abs(q[1] - w[1]) # 거리 계산
            if cnt > distance:
                cnt = distance
        t += cnt
    if t < res:
        res = t

print(res)