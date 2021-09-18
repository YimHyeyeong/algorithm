tc = int(input())

for t in range(1, tc +1):
    lst = list(map(int,input().strip()))

    n = [0] * 12
    for i in range(len(lst)):
        n[lst[i]] += 1

    i = 0
    cnt = 0
    while i <10:
        if n[i] >= 3:
            n[i] -= 3
            cnt += 1
            continue
        if n[i] >= 1 and n[i+1] >= 1 and n[i+2] >= 1:
            n[i] -= 1
            n[i+1] -= 1
            n[i+2] -= 1
            cnt += 1
            continue

        i += 1

    if cnt == 2:
        print('#{} Baby Gin'.format(t))
    else:
        print('#{} Lose'.format(t))

