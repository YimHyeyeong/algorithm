from sys import stdin
dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]

def func(x,y):
    q = []
    q.append((x,y))
    arr[x][y] = 0
    while q:
        r,c = q.pop(0)
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < h and 0 <= nc < w:
                if arr[nr][nc] == 1:
                    q.append((nr,nc))
                    arr[nr][nc] = 0


while True:
    w,h = map(int, stdin.readline().split())
    if w == h == 0:
        break
    arr = [list(map(int, stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                func(i,j)
                cnt += 1
    print(cnt)