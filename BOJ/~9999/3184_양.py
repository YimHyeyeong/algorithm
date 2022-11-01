# 1

from sys import stdin
from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def func(x,y):
    global sheep, wolf
    s = w = 0
    q = deque()
    q.append((x,y))
    if arr[x][y] == 'o':
        s += 1
    if arr[x][y] == 'v':
        w += 1
    visited[x][y] = 1
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] != '#':
                q.append((nr,nc))
                if arr[nr][nc] == 'o':
                    s += 1
                if arr[nr][nc] == 'v':
                    w += 1
                visited[nr][nc] = 1

    if s > w:
        sheep += s
    else:
        wolf += w

R,C = map(int, stdin.readline().split())

arr = [stdin.readline().rstrip() for _ in range(R)]


sheep = wolf = 0
visited = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and not visited[i][j]:
            func(i,j)
print(sheep, wolf)




# 2

from sys import stdin
from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def func(x,y):
    global sheep, wolf
    s = w = 0
    q = deque()
    q.append((x,y))
    while q:
        r,c = q.popleft()
        if arr[r][c] == 'o':
            s += 1
        if arr[r][c] == 'v':
            w += 1
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] != '#' and (nr,nc) not in q:  # 중복되는 곳을 걸러줌
                q.append((nr,nc))

    if s > w:
        sheep += s
    else:
        wolf += w

R,C = map(int, stdin.readline().split())

arr = [stdin.readline().rstrip() for _ in range(R)]


sheep = wolf = 0
visited = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and not visited[i][j]:
            func(i,j)
print(sheep, wolf)