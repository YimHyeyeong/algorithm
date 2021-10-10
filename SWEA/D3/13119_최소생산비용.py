def func(level, res):
    global val
    if res >= val: # 가지치기, 더하는 와중에 이전에 값보다 크다면 굳이 더 볼 필요없이 리턴
        return
    if level == N:
        if res < val:
            val = res
        return

    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        func(level + 1, res + arr[level][i])  
        used[i] = 0



tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * N
    val = 21e8
    func(0,0)
    print('#{} {}'.format(t,val))