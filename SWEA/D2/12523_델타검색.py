for i in range(1, 11):

    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    total = 0
    for y in range(N):
        for x in range(N):
            for t in range(4):
                ny = y +dy[t]
                nx = x +dx[t]
                if ny < 0 or nx < 0 or ny >= N or nx >= N:
                    continue
                total += abs(lst[y][x]-lst[ny][nx])
    print('#{} {}'.format(i, total))
