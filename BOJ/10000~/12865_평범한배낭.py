from sys import stdin

N, K = map(int,stdin.readline().split())
lst = [[0,0]] # 0 인덱스 처리, 안해주면 j-w할 때를 고려
for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))

dp = [[0] * (K+1) for _ in range(N+1)] # 행과 열에 +1 해줘야 이전 값을 참고할 때(i-1) 에러 안남.. 

for i in range(1,N+1): # lst 배열 돌기(행)
    for j in range(1,K+1): # 무게 돌기 (열)
        w = lst[i][0] # 무게
        v = lst[i][1] # 가치

        if j < w : # 배낭에 넣을 수 있는 무게보다 무거우면 어쨋든 못넣으니까
            dp[i][j] = dp[i-1][j] # 이전(윗행)이 현재까지 그 무게에서의 가장 큰 가치를 저장한 것이기 때문에 윗행렬의 가치를 가져옴
        else:
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w] + v) # 지금 들고 있는 물건의 무게를 뺀 무게(현재 물건을 넣을 수 있는 무게 확보)에서의 가장 큰 가치와 현재 물건의 가치

print(dp[N][K])


# 0 ~ K까지 하나씩 돌면서 어떤 물건을 넣었을 경우 가장 가치가 큰지 확인
# 표를 그려봐야 함. 위에서 아래에서 표를 돌면서 그때마다 가장 가치가 큰 것을 dp에 저장
# max(dp[i-1][j] , dp[i-1][j-w] + v) -> 안에 있는 물건을 빼고 새로운 물건을 넣어야 하는지 아니면 그대로 가야하는 지 선택하는 과정