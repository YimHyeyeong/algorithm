tc= int(input())

for t in range(1, tc+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r,c = 0, -1
    cnt = 1
    k = 0
    while cnt <= n*n:
        nr, nc = r + dr[k], c + dc[k]
        if 0<= nr < n and 0 <= nc < n and arr[nr][nc] ==0:
            arr[nr][nc] = cnt
            cnt += 1
            r,c = nr, nc

        else:
            k = (k+1) % 4


    print('#{}'.format(t))
    for i in range(n):
        print(*arr[i])