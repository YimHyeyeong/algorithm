from sys import stdin
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def func(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        r,c = q.popleft()
        if r == (N-1) and c == (M-1):
            return visited[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc))


N, M = map(int, stdin.readline().split())

arr = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * (M+1) for _ in range(N+1)]
print(func(0,0))