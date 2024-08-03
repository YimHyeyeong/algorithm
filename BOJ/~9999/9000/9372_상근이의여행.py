from sys import stdin

def func(n):
    global cnt
    visited[n] = 1
    for i in arr[n]:
        if visited[i] == 0:
            cnt += 1
            func(i)


T = int(stdin.readline())
for _ in range(T):
    N,M = map(int, stdin.readline().split())
    arr = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    for _ in range(M):
        a,b = map(int, stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)
    func(1)
    print(cnt)