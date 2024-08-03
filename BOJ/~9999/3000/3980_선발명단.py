from sys import stdin

def func(n, cnt):
    global res
    if n == 11:
        if cnt > res:
            res = cnt
        return

    for i in range(11):
        if not visited[i] and arr[n][i]: # 가지치기
            visited[i] = 1
            func(n+1, cnt + arr[n][i])
            visited[i] = 0

            
T = int(stdin.readline())

for _ in range(T):
    arr = [list(map(int,stdin.readline().split())) for _ in range(11)]

    visited = [0] * 11 # 포지션 체크
    res = -21e8
    func(0,0)
    print(res)