from sys import stdin

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for j in range(1,N+1):
        if visited_dfs[j] == 0 and edge[v][j] == 1:
            dfs(j)


def bfs(v):
    q = []
    visited_bfs = [0] * (N+1)
    q.append(v)
    visited_bfs[v] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for k in range(1, N+1):
            if edge[t][k] == 1 and visited_bfs[k] == 0:
                q.append(k)
                visited_bfs[k] = 1


N, M, V = map(int,stdin.readline().split())

edge = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, stdin.readline().split())
    edge[a][b] = edge[b][a] = 1

visited_dfs = [0] * (N+1)

dfs(V)
print()
bfs(V)