# 1. 상어가 있는 1을 기준으로 bfs 도는 버전
from sys import stdin
from collections import deque

dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]

def func():
    while q:
        r,c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr,nc))

    return


N, M = map(int, stdin.readline().split())

arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

q = deque()

for j in range(N):
    for k in range(M):
        if arr[j][k] == 1:
            q.append((j,k)) # 먼저 1을 다 큐에 넣어줘야 가장 가까운 상어와의 안전거리를 구할 수 있음
func()

res = 0
for q in range(N):
    for w in range(M):
        res = max(res, arr[q][w])

print(res -1)


# 2. 0을 기준으로 bfs 돌리는 버전

from sys import stdin
from collections import deque

dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]

def func(x,y,cnt):
    visited = [[0] * M for _ in range(N)] # 방문표시
    q = deque()
    q.append((x,y,cnt))
    visited[x][y] = 1
    while q:
        r,c,t = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 0:
                    q.append((nr,nc, t + 1))
                    visited[nr][nc] = 1
                else: # 상어를 만날 때 까지
                    return t + 1 # 0부터 시작이니까 + 1 해주기


N, M = map(int, stdin.readline().split())

arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
res = 0
for j in range(N):
    for k in range(M):
        if arr[j][k] == 0: # 0에서 1이 있는 자리까지의 거리
            res = max(res, func(j,k,0))

print(res)
