tc = 10

for t in range(1, tc+1):
    N = int(input())

    lst = list(map(int,input().split()))

    cnt = 0
    for i in range(1 << N):
        val = 0
        for j in range(N):
            if i & (1<<j):
                val += lst[j]
        if val == 0:
            cnt += 1
    print('#{} {}'.format(t,cnt))

