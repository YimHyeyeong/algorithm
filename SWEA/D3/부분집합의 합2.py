T = int(input())

for i in range(1, T+1):


    lst = list(range(1, 13))

    N, K = map(int, input().split())
    res = 0
    for j in range(1<<12):
        total = 0
        cnt = 0
        for k in range(12):
            if j & (1<< k):
                total += lst[k]
                cnt += 1
        if total == K and cnt == N:
            res += 1

    print('#{} {}'.format(i,res))