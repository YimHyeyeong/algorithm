for i in range(1,11):
    t = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]

    max_1 = 0
    for r in range(100):
        sum_1 = 0
        for c in range(100):
            sum_1 += lst[r][c]
        if sum_1 > max_1:
            max_1 = sum_1

    max_2 = 0
    for r in range(100):
        sum_2 = 0
        for c in range(100):
            sum_2 += lst[c][r]
        if sum_2 > max_2:
            max_2 = sum_2


    max_3 = 0
    for r in range(100):
        sum1 = 0
        sum2 = 0
        sum1 += lst[r][r]
        sum2 += lst[r][99-r]
    if max(sum1, sum2) > max_3:
        max_3 = max(sum1, sum2)


    res = max(max_1, max_2, max_3)

    print('#{} {}'.format(t, res))






