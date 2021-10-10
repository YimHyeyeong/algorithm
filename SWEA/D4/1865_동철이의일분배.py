#[1]
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



############
#[2]

def backtrack(k, p):
    global ans
    if ans >= p: return  # 0 ~ 1 을 곱하니까 더 큰 값이 나올 수 없다.
    if k == N:
        ans = p
    else:
        for i in range(N):
            if used[i]: continue
            used[i] = 1
            # 순서를 저장할 필요 없다
            # k번 직원에게 i번 일을 배정
            backtrack(k + 1, p * arr[k][i])
            used[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(lambda x: float(x)/100, input().split())) for _ in range(N)]
    used = [0] * N
    ans = 0
    backtrack(0, 100.0)
    print('#{} {:.6f}'.format(tc, ans))
