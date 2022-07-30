from sys import stdin

def func(s):
    global cnt
    visited[s] = 1
    for i in lst[s]:
        if visited[i] == 0:
            func(i)
            cnt += 1


N = int(stdin.readline())
M = int(stdin.readline())

lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(M):
    a,b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)


func(1)
print(cnt)