def func(level):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if used[i] == 1: continue
        elif hap[level+i] == 1: continue
        elif cha[level - i + N] == 1: continue  # 음수 방지하기 위해 + @
        used[i] = 1
        hap[level + i] =1
        cha[level - i + N] =1
        func(level+1)
        used[i] = 0
        hap[level + i] = 0
        cha[level - i + N] = 0

tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    used = [0] * N
    hap = [0] * (2*N)  # / 체크 , 각각의 인덱스를 더하면 / 방향으로 숫자가 같음
    cha = [0] * (2*N)  # \ 체크 , 각각의 인덱스를 빼면 \방향으로 숫자가 같음
    cnt = 0
    func(0)
    print('#{} {}'.format(t,cnt))