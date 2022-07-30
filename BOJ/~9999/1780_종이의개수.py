def func(x,y,n):
    global res
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                func(x,y,n//3)
                func(x+n//3, y, n//3)
                func(x+n//3*2,y, n//3)

                func(x, y+n//3, n//3)
                func(x, y+n//3*2, n//3)

                func(x+n//3, y+n//3, n//3)
                func(x + n // 3, y + n // 3*2, n // 3)

                func(x + n // 3*2, y + n // 3, n // 3)
                func(x + n // 3 * 2, y + n // 3*2, n // 3)

                return
    res[color] += 1


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

res = [0,0,0]
func(0,0,N)
print(res[-1])
print(res[0])
print(res[1])