# [1]

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

######################################
# [2]

tc = 10
for t in range(1, tc +1):
    N = int(input())
    lst = []
    for i in range(100):
        tmp = list(map(int, input().split()))
        lst.append(tmp)

    res = []

    for i in range(len(lst)):
        row_sum = 0
        for j in range(len(lst[i])):
            row_sum += lst[i][j]
        res.append(row_sum)

    for j in range(len(lst[0])):
        col_sum = 0
        for i in range(len(lst)):
            col_sum += lst[i][j]
        res.append(col_sum)

    for i in range(len(lst)):
        sum1 = 0
        for j in range(len(lst[i])):
            if i == j:
                sum1 += lst[i][j]
        res.append(row_sum)

    for i in range(len(lst)):
        sum2 = 0
        for j in range(len(lst[i])):
            if i == len(lst)-j:
                sum2 += lst[i][j]
        res.append(row_sum)


    print(f'#{t} {max(res)}')

