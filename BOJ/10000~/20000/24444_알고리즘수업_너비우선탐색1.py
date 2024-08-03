from sys import stdin
from collections import deque

def bfs():
    q = deque()
    q.append(R)
    cnt = 1
    visited[R] = cnt
    while q:
        c = q.popleft()
        for i in adj[c]:
            if not visited[i]:
                q.append(i)
                cnt +=1
                visited[i] = cnt

N, M,R = map(int, stdin.readline().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, stdin.readline().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

visited = [0] * (N+1)
for ad in adj:
    ad.sort()
bfs()
for j in visited[1::]:
    print(j)