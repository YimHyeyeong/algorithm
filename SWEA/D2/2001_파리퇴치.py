tc = int(input())

for t in range(1, tc +1):
    n,m =map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]

    total = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m):
                for q in range(m):
                    cnt += arr[i+k][j+q]

            if cnt > total:
                total = cnt

    print('#{} {}'.format(t,total))