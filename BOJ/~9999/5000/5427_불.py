from sys import stdin
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def fire_move():
    for _ in range(len(fire)): # 배열의 크기만큼만 돌려야 불 - 상근 - 불 - 상근 순서대로 할 수 있음 (while x)
        r, c = fire.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] != '#' and arr[nr][nc] != '*':
                arr[nr][nc] = '*'
                fire.append((nr,nc))


def sang_move():
    res = False # 갈 수 있는지 확인
    for _ in range(len(sang)):
        r, c = sang.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc] and arr[nr][nc] != '#' and arr[nr][nc] != '*':
                    res = True # 갈 수 있음
                    visited[nr][nc] = visited[r][c] +1 # 이동하는 시간 저장
                    sang.append((nr,nc))
            else: # 배열 밖을 벗어나면 건물 밖을 벗어난 것
                return visited[r][c]
    if not res: # 계속 False면 못 빠져나간 것
        return "IMPOSSIBLE"

T = int(stdin.readline())

for _ in range(T):
    w, h = map(int , stdin.readline().split())

    fire, sang = deque(), deque()
    arr = [list(stdin.readline().strip()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*': # 불들이 시작하는 위치 저장
                fire.append((i,j))
            if arr[i][j] == '@': # 상근이 시작 위치 저장
                sang.append((i,j))

    visited = [[0] * w for _ in range(h)]
    visited[sang[0][0]][sang[0][1]] = 1 # 상근이 시작 위치 방문 표시 

    while True:
        fire_move()
        ans = sang_move()
        if ans: # 상근이가 빠져나오거나 빠져나오지 못 할 경우 return 값이 있음
            break
    print(ans)