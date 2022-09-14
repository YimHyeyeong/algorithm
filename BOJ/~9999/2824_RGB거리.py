from sys import stdin

N = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]

for i in range(1,N):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2]) # 연속되는 색깔이면 안됨
    arr[i][1] += min(arr[i-1][0], arr[i-1][2]) # 1번 색을 선택하고 이전에 집에서는 1번을 제외한 색깔을 선택하는 경우
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])

print(min(arr[N-1]))