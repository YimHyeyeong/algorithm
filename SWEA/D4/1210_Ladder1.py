#[1]
tc = 10

for t in range(1, tc + 1):

    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]


    j = 0

    for goal in range(100):
        if arr[99][goal] == 2:
            j = goal


    i =99

    while i >0 :
        i -= 1

        if j > 0 and arr[i][j-1] == 1:
            while j >0 and arr[i][j-1]:
                j -= 1


        elif j < 99 and arr[i][j+1] == 1:
            while j < 99 and arr[i][j+1]:
                j += 1


    print('#{} {}'.format(t,j))


######################
#[2]

T = 10
for t in range(T):
    test = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    d_y = N-1
    d_x = ladder[N-1].index(2)
    move = 0
    while d_y > 0:
        if (move == 0 or move == 1) and d_x > 0 and ladder[d_y][d_x-1]:
            d_x -= 1
            move = 1
        elif (move == 0 or move == 2) and d_x < N-1 and ladder[d_y][d_x+1]:
            d_x += 1
            move = 2
        else:
            d_y -= 1
            move = 0
    print("#{} {}".format(test, d_x))