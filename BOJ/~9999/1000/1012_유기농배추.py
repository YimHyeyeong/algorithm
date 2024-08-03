from sys import stdin

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def func(x,y):
    q = []
    q.append((x,y))
    arr[x][y] = 0
    while q:
        r,c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    q.append((nr,nc))



T = int(stdin.readline())
for _ in range(T):
    M,N,K = map(int,stdin.readline().split())
    arr = [[0] * M for _ in range(N)]

    for _ in range(K):
        a,b = map(int, stdin.readline().split())
        arr[b][a] = 1


    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                func(i,j)
                cnt += 1

    print(cnt)