# 분할정복
def func(x,y,n):
    global white, blue

    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                func(x,y,n//2) # 왼쪽 위
                func(x,y+n//2, n//2) # 왼쪽 아래
                func(x+n//2, y, n//2) # 오른쪽 위
                func(x+n//2, y+n//2, n//2) # 오른쪽 아래
                return
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
func(0,0, N)
print(white)
print(blue)