from sys import stdin

N = int(stdin.readline())
lst = list(stdin.readline().rstrip())
arr = [[0] * 101 for _ in range(101)] # lst의 길이가 최대 50자이기 때문에 아래 위로 50씩 해서 101

dr = [1,0,-1,0] # 하 우 상 좌
dc = [0,1,0,-1]

R = C = startR = startC = endR = endC = 50 # 시작 지점이 (50,50)
arr[R][C] = 1

dir = 0 # 남쪽을 바라보고 있기 때문에 0부터 시작
for i in lst:
    if i == 'L':  # 좌로 90도 돌기
        dir = (dir + 1) % 4 
        continue # 이동은 안함
    elif i == 'R': 
        dir = (dir + 3) % 4
        continue
    
    # i == F일 경우
    R += dr[dir] # 바라보고 있는 방향으로 한 칸 이동
    C += dc[dir]
    arr[R][C] = 1 # 방문 표시

    if R < startR: # 시작 지점보다 위로 올라가면
        startR = R
    if R > endR: # 시작 지점보다 아래로
        endR = R
    if C < startC: # 시작 지점보다 왼쪽으로
        startC = C
    if C > endC: # 시작 지점보다 오른쪽으로
        endC = C

for r in range(startR, endR+1):
    for c in range(startC, endC+1):
        if arr[r][c]:
            print('.', end='')
        else:
            print('#', end='')
    print()

