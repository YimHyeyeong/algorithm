def func(x,y,n):
    global res
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                res.append("(")
                func(x, y, n // 2)
                func(x, y+n//2, n//2)
                func(x+n//2, y, n//2)

                func(x+n//2, y+n//2, n//2)
                res.append(")")
                return
    res.append(color)



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
res = []
func(0,0,N)
print("".join(map(str,res)))
