T = 10
for t in range(1, T+1):
    input()
    password = list(map(int, input().split()))
    i = 1
    while True:
        a = password.pop(0) - i

        if a < 0: a = 0
        password.append(a)

        if a <= 0: break
        i += 1

        if i > 5: i = 1
    print('#{} '.format(t), end='')
    print(*password)