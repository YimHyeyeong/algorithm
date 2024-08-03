from sys import stdin
import math
def func(n):
    for a in range(2, int(math.sqrt(n))+1):
        if not n % a:
            return False
    return True

N = int(stdin.readline())

lst = []

for i in range(2, N+1):
    if func(i):
        lst.append(i)
dp = [0] * (N+1)
dp[0] = 1
for k in lst:
    for q in range(k,N+1):
        dp[q] = (dp[q] + dp[q-k])%123456789

print(dp[N])