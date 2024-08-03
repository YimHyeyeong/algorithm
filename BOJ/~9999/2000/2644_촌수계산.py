from sys import stdin

def func(node):
    for i in lst[node]: # 연결된 노드
        if not visited[i]: # 방문하지 않은 경우
            visited[i] = visited[node] + 1 # 출발점에서 얼마나 떨어진지
            func(i)

n = int(stdin.readline())
p,c = map(int,stdin.readline().split())

lst = [[] * (n+1) for _ in range(n+1)] 
for _ in range(int(stdin.readline())):
    a,b = map(int,stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [0] * (n+1) # 노드 이동거리 저장
func(p)
print(visited[c] if visited[c] else -1)