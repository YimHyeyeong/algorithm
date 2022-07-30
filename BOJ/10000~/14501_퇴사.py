from sys import stdin

N = int(stdin.readline())

lst = [list(map(int,stdin.readline().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N-1,-1,-1):
    if lst[i][0] + i > N:
        dp[i] = dp[i+1]
    else:
        # 앞(max_arr[i+1])에서 얻은 최댓값 vs 
        # 현재의 일을 끝마친 후 얻을 수 있는 최대값(arr[i][1] + max_arr[i+arr[i][0]])
        # 중 더 큰 수를 현재 최대값으로 저장
        dp[i] = max(dp[i+1], lst[i][1] + dp[i+lst[i][0]])
print(dp[0])