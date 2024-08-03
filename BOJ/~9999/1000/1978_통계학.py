from sys import stdin


N = int(stdin.readline())

lst = list(map(int, stdin.readline().split()))
res = 0
for i in lst:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else: # 안해주면 틀림~
        res += 1
print(res)