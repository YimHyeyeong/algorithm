from sys import stdin


N = int(stdin.readline())

for i in range(1, N+1):
    sum_num = sum(map(int, str(i)))
    new_num = sum_num + i
    if new_num == N:
        print(i)
        break
    elif i == N:
        print(0)