N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

cnt = end = 0
for s,e in arr:
    if s >= end:
        cnt += 1
        end = e

print(cnt)