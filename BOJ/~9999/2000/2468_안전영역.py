from sys import stdin
from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def func(x,y, h):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc <N and not visited[nr][nc] and arr[nr][nc] > h:
                visited[nr][nc] = 1
                q.append((nr,nc))


N = int(stdin.readline())

arr = [list(map(int,stdin.readline().split())) for _ in range(N)]

res = -21e8

for i in range(101): # 높이의 최대가 100임
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > i:
                func(r,c,i)
                cnt +=1

    if cnt > res:
        res = cnt

print(res)
