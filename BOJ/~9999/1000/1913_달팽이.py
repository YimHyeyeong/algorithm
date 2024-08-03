from sys import stdin


N = int(stdin.readline())

num = int(stdin.readline())
num_x = num_y = 0
arr = [[0] * N for _ in range(N)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

cnt = N ** 2
r = c = 0
arr[r][c] = cnt # (0,0)에서  시작
cnt -= 1
dir = 0 # 방향 저장

while cnt > 0:
    nr = r + dr[dir]
    nc = c + dc[dir]

    if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]: # 표를 벗어나거나 이미 숫자가 저장되어 있는 경우
        arr[nr][nc] = cnt

        if cnt == num: # 찾아야 하는 좌표를 만났을 경우
            num_x, num_y = nr, nc # 좌표 저장
        cnt -= 1
        r,c = nr, nc 
    else:
        dir = (dir + 1) % 4 # 방향변경

for i in arr:
    print(*i)
print(num_x+1, num_y+1)