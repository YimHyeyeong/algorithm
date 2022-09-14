from sys import stdin

def func(n): # n과 연결된 곳들 체크하는 함수
    for i in adj[n]:
        if not visited[i]:
            visited[i] = 1
            func(i)

N,M = map(int,stdin.readline().split())

adj = [[] for _ in range(N+1)] # 연결되어 있는 노드들 담기

for _ in range(M):
    a,b = map(int,stdin.readline().split())
    adj[a].append(b) # 방향이 없는 그래프라서 둘 다 넣어주기
    adj[b].append(a)

visited = [0] * (N+1) # 방문표시
cnt = 0 # 연결요소 개수 체크

for j in range(1, N+1):
    if not visited[j]: # 방문하지 않았다면 다른 연결 요소라는 것
        cnt += 1
        func(j)

print(cnt)