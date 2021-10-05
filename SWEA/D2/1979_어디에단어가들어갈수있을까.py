tc = int(input())

for t in range(1, tc+1):

    n,k = map(int, input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]


    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1

            if arr[i][j] == 0 or j == n-1:
                if cnt == k:
                    total   += 1
                cnt = 0

        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1

            if arr[j][i] == 0 or j == n-1:
                if cnt == k:
                    total += 1
                cnt = 0

    print('#{} {}'.format(t, total))



