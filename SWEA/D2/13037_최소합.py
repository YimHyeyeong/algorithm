# [1]
def func(r,c, res):
    global total
    if r == c == N-1: # 맨 오른쪽 아래에 도달하면
        res += arr[r][c]  # 오른쪽 아래의 값을 더함
        if total > res:
            total = res
            return

    dr = [1,0] # 오른쪽이랑 아래로만 이동할 수 있으니까 2개만
    dc = [0,1]
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            func(nr, nc,res+arr[r][c]) # res에 원래 있던 자리의 값을 더함


tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total = 10000

    func(0,0,0)
    print('#{} {}'.format(t,total))



######
# [2]
def dfs(y,x):
    if y >= N or x >= N : return int(21e8) # 범위 벗어날때 정답에 영향 미치지 않은 값으로 리턴한다.
    if y == N-1 and x == N-1 :
        return MAP[y][x]

    a = dfs(y,x + 1)
    b = dfs(y+1, x)

    return min(a,b) + MAP[y][x]

T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    MAP = [
        list(map(int, input().split())) for _ in range(N)
    ]

    ret = dfs(0,0)
    print("#{} {}".format(tc, ret))