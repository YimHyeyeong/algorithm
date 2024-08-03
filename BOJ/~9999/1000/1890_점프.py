from sys import stdin
from collections import deque

N = int(stdin.readline())

arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]  # 해당 위치에 올 수 있는 방법을 저장하는 배열

dp[0][0] = 1

for i in range(N):  # for 문을 돌면서 [i][j]에서 갈 수 있는 위치들에 +1 해줌
    for j in range(N):
        if i == N-1 and j == N-1: # 왼쪽 아래에 도착한다면
            break

        d = i + arr[i][j] # i는 현재 있는 위치의 행 + 갈 수 있는 칸 수 (밑으로) 
        r = j + arr[i][j] # i는 현재 있는 위치의 행 + 갈 수 있는 칸 수 (오른쪽) 

        if d < N: # 배열 밖으로 벗어나지 않는다면
            dp[d][j] += dp[i][j] # dp 배열에 갈 수 있는 경우의 수를 저장 
        if r < N:
            dp[i][r] += dp[i][j] # 이전의 위치([i][j])까지 갈 수 있는 경우의 수를 이동할 수 있는 위치에 저장하기
print(dp[N-1][N-1])