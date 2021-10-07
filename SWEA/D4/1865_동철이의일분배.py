def func(level, res):
    global val
    if res <= val:  # 등호들어가야지 에러안남 아니면 시간초과
        return
    if level == N:
        if res > val:
            val=res
        return
    for i in range(N):
        if used[i]: continue
        used[i] = 1
        S = arr[level][i] / 100
        func(level + 1, res * S)
        used[i] = 0


tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * N
    val = -21e8
    func(0,100)
    print("#{} {:.6f}".format(t, val,3))

