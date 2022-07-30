from sys import stdin

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def func(x,y):
    q = []
    q.append((x,y))
    lst[x][y] =0
    t = 1
    while q:
        r, c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if lst[nr][nc] == 1:
                    lst[nr][nc] = 0
                    q.append((nr,nc))
                    t += 1
    res.append(t)




N = int(stdin.readline())
lst = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]
res = []
cnt = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            func(i,j)
            cnt += 1
res.sort()
print(cnt)
for w in range(len(res)):
    print(res[w])