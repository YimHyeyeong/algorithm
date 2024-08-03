from sys import stdin
from collections import deque


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def func(x,y):
    q = deque()
    q.append((x,y))
    arr[x][y] = 2
    num = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nr = a + dr[i]
            nc = b + dc[i]
            if 0 <= nr < M and 0 <= nc < N and not arr[nr][nc]:
                q.append((nr,nc))
                arr[nr][nc] = 2
                num += 1

    return num


M,N,K = map(int,stdin.readline().split())

arr = [[0] * N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int, stdin.readline().split())
    for i in range(y1,y2): # 주어진 배열을 상하로 뒤집어도 영역을 구하는 것은 똑같음
        for j in range(x1,x2): 
            arr[i][j] = 1

cnt = 0
lst = []
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0:
            lst.append(func(r,c))
            cnt += 1

print(cnt)
print(*sorted(lst))
