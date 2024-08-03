from sys import stdin
from itertools import permutations  # 순열 생성

N, K = map(int, stdin.readline().split())

lst = list(map(int, stdin.readline().split()))
res = 0

for i in permutations(lst, N):
    cnt = 500
    for j in range(N):
        cnt -= K
        cnt += i[j]
        if cnt < 500:
            break
        if j == N-1:
            res += 1

print(res)