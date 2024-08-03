from sys import stdin

def func(k):
    for i in range(N):
        if arr[k][i] and not visited[i]:
            visited[i] = 1
            func(i)


N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
for i in range(N):
    visited = [0] * N # i의 노드에서 갈 수 있는 경로 저장
    func(i)
    print(*visited)