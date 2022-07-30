from sys import stdin

def func(s):
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        for i in lst[t]:
            if not visited[i]:
                res[i] = t
                q.append(i)
                visited[i] = 1

N = int(stdin.readline())
lst = [[] for _ in range(N+1)]

visited = [0] * (N+1)
res = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)


func(1)
for j in res[2:]:
    print(j)