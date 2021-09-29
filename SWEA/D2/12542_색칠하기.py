tc = int(input())

for t in range(1, tc +1):
    n = int(input())

    arr = [[0]*10 for _ in range(10)]

    for i in range(n):
        a1, a2, b1, b2, c = map(int,input().split())

        for x in range(a1, b1+1):
            for y in range(a2, b2+1):
                arr[x][y] += c

    cnt = 0
    for j in range(10):
        for k in range(10):
            if arr[j][k] ==3:
                 cnt += 1

    print('#{} {}'.format(t,cnt))
