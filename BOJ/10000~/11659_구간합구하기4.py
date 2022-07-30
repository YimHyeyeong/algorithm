from sys import stdin

N, M = map(int, stdin.readline().split())

lst = list(map(int, stdin.readline().split()))
arr = [list(map(int,stdin.readline().split())) for _ in range(M)]

res = [0]
cnt = 0
for i in lst:
    cnt += i
    res.append(cnt)

for j,k in arr:
    a = res[k]
    b = res[j-1]
    print(a-b)