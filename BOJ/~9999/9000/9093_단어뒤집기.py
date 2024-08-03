from sys import stdin

N = int(stdin.readline())

lst = [list(stdin.readline().split()) for _ in range(N)]
for i in lst:
    for j in i:
        print(j[::-1], end=' ')
    print()