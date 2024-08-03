from sys import stdin

while True:
    n = int(stdin.readline())
    if n == -1:
        break

    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)

    if sum(lst) == n:
        print(n,'=', end=' ')
        print(*lst, sep=' + ')
    else:
        print("{} is NOT perfect." .format(n))