#[1]
def func(level, sum, cnt):
    global  total
    if cnt == N-1:  # 모든 관리구역을 다 돌았으면
        sum += arr[level][0]  # 다시 출발지로 복귀하는 값을 더함
        if sum < total:
            total = sum

        return

    for i in range(N):
        if arr[level][i] == 0 :continue  # 0인 곳(연결되지x)은 넘기고
        if visited[i] == 1: continue # 이미 방문한 곳은 넘기고
        visited[i] = 1  # 먼저 방문 표시하고
        func(i, sum+arr[level][i], cnt+1)  # sum에 방금 있던 곳을 더함
        visited[i] = 0


tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N  # 방문한 곳 표시
    visited[0] = 1  # 출발지는 먼저 1표시
    total = 21e8
    func(0,0,0)
    print('#{} {}'.format(t, total))


