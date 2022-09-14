from sys import stdin
N,M=map(int,stdin.readline().split())

arr = [list(map(int,stdin.readline().split())) for _ in range(N)]

dp = [[0] * (M+1) for _ in range(N+1)]  # dp 값을 저장할 배열, 위, 왼쪽, 왼쪽위 대각선을 봐야해서 행,열 한 줄씩 추가

for i in range(1, N+1): # 값이 시작하는 1부터 시작
    for j in range(1, M+1):
        # arr에 있는 기존의 값 + 왼쪽, 위, 왼쪽 대각선 중 가장 큰 값
        dp[i][j] = arr[i-1][j-1] + max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[N][M])