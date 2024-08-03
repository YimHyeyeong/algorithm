from sys import stdin

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def func(x,y, cnt):
    global res  

    if cnt > K: # K보다 돌아가는 경로일 경우 리턴
        return

    if x == 0 and y == C - 1:
        if cnt+1 == K:
            res += 1
        return

    visited[x][y] = 1

    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0<= nr < R and 0<= nc < C and visited[nr][nc] == 0 and arr[nr][nc] != 'T':
            func(nr,nc, cnt +1)
            visited[nr][nc] = 0


R, C, K = map(int, stdin.readline().split())

arr = [list(stdin.readline().rstrip()) for _ in range(R)]

visited = [[0] * C for _ in range(R)]
res = 0
func(R-1, 0, 0)
print(res)
