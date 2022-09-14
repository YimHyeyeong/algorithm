from sys import stdin

N = int(stdin.readline())

lst = [stdin.readline().rstrip() for _ in range(N)]

for i in lst:
    i = i[::-1]
    for j in lst:
        if i == j:
            print(len(i), i[len(i)//2])
            exit()


