from sys import stdin
from collections import deque

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        t = q.popleft()
        for i in arr[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1 # 방문 순서 저장


N, M = map(int , stdin.readline().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (N+1)
bfs()
min_num = visited.index(max(visited))
count_num = visited.count(max(visited))
print(min_num, visited[min_num]-1, count_num)