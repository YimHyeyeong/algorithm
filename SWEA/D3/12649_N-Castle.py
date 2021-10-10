def func(level):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if used[i] == 1 : continue
        used[i]=1 # 방문표시
        func(level + 1)
        used[i] = 0
for t in range(1,11):
    N = int(input())
    used = [0] * N
    cnt = 0
    func(0)
    print('#{} {}'.format(t,cnt))