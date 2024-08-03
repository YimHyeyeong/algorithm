from sys import stdin
# 14501 퇴사 문제와 같음 
N = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if lst[i][0] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], lst[i][1] + dp[i+lst[i][0]])

print(dp[0])