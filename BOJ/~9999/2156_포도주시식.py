from sys import stdin

n = int(stdin.readline())

lst = [int(stdin.readline()) for _ in range(n)]

dp = [0] * (n+1)
dp[1] = lst[0] # 맨 처음 와인양 저장

if n > 1:
    dp[2] = lst[1] + lst[0] # 두번째 와인과 첫번째 와인 합한 값을 저장


# 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. c
# 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. b
# 현재 포도주를 마시지 않는다. a
# 예를들어 5번째에 오는 와인(인덱스로는 4)까지 최대로 마실 수 있는 경우는
# 1245 / 235 / 134 번째에 있는 와인들을 선택하는 경우이다
# 1245(=c의 경우)는 전전전 포도주에서 고를 수 있는 최댓값(12) + 바로 이전의 포도주(4) + 현재 포도주(5)
# 235(=b)는 전전 포도주(23) + 현재 포도주(5)
# 134(=c)는 현재 포도주를 건너뛰고 바로 이전의 포도주까지의 최댓값(134)
# 그 중 최댓값을 골라 dp에 저장  
for i in range(3, n+1):
    a = dp[i-1] # dp[i-2] + lst[i-2]로 표기하지 않는 이유는 dp[i-1]에 해당 케이스를 포함한 최댓값이 저장되어 있기때문
    b = dp[i-2] + lst[i-1]
    c = dp[i-3] + lst[i-2] + lst[i-1]
    dp[i] = max(a,b,c)

print(dp)