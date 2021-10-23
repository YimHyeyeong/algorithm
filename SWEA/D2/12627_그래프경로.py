def func(now):
    for j in range(1,V+1):
        if visited[j] == 1: continue
        if MAP[now][j] == 0:continue
        visited[j] = 1
        func(j)

tc = int(input())

for t in range(1,tc+1):
    V, E = map(int,input().split())
    MAP = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        a,b = map(int,input().split())
        MAP[a][b] = 1

    S,G = map(int,input().split())
    visited = [0 for _ in range(V + 1)]
    visited[S] = 1

    func(S)
    print('#{}'.format(t) , end=' ')
    if visited[G] == 1:
        print(1)
    else:
        print(0)


