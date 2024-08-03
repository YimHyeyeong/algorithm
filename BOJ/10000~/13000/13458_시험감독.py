from sys import stdin

N = int(stdin.readline())
lst = list(map(int,stdin.readline().split()))
B,C = map(int, stdin.readline().split())

total = 0
for i in lst:
    res = i - B
    total += 1
    if res > 0 : # while문 돌면 시간초과남
        if res % C == 0:
            total += res // C
        else:
            total += int(res / C+1)
print(total)

