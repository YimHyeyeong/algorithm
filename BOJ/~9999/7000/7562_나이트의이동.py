from sys import stdin
from collections import deque

dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]

def func(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        r,c = q.popleft()
        if r == move_x and c == move_y:
            return visited[r][c]-1

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <= I-1 and 0 <= nc <= I-1:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1 # 이전 움직인 횟수에 +1 하면 현재 위치까지 움직인 횟수가 됨
                    q.append((nr,nc))



T = int(stdin.readline())
for _ in range(T):
    I = int(stdin.readline())
    now_x, now_y = map(int, stdin.readline().split())
    move_x, move_y = map(int, stdin.readline().split())
    visited = [[0] * (I+1) for _ in range(I+1)]  # 움직인 횟수 저장
    print(func(now_x, now_y))
