from sys import stdin

n,m = map(int,stdin.readline().split())
queen = list(map(int,stdin.readline().split()))
knight = list(map(int,stdin.readline().split()))
pawn = list(map(int,stdin.readline().split()))

visited = [[0] * m for _ in range(n)]

# pawn 위치 저장
for i in range(1, pawn[0]*2, 2):
    r, c = pawn[i]-1, pawn[i+1]-1
    visited[r][c] = 2 # 장애물이 놓이는 위치와 이동할 수 있는 위치를 구별하기 위해

# knight
kr = [-2,-2,-1,1,2,2,1,-1]
kc = [-1,1,2,2,1,-1,-2,-2]

for j in range(1, knight[0]*2, 2):
    r,c = knight[j]-1, knight[j+1]-1
    visited[r][c] = 2 # 장애물이 놓이는 위치와 이동할 수 있는 위치를 구별하기 위해
    for k in range(8):
        nr = r + kr[k]
        nc = c + kc[k]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = 1


qr = [-1,-1,-1,0,1,1,1,0]
qc = [-1,0,1,1,1,0,-1,-1]
for q in range(1, queen[0]*2, 2):
    r,c = queen[q]-1, queen[q+1] -1
    visited[r][c] = 1
    for w in range(8):
        tr,tc = r,c
        while True:
            nr = tr + qr[w]
            nc = tc + qc[w]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] == 2: # 체스판을 벗어나지 않고 장애물이 아니라면
                visited[nr][nc] = 1
                tr,tc = nr,nc
            else:
                break

cnt = 0
for m in visited:
    for v in m:
        if not v:
            cnt +=1

print(cnt)


