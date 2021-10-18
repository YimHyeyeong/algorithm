def same(str):
    for i in range(len(str)):
        if str[i] != str[len(str)-1-i]:
            return 0
    return 1

tc = int(input())

for t in range(1, tc+1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    ans =''
    for i in range(N):
        for j in range(N-M+1):
            tmp = arr[i][j:j+M]
            res = same(tmp)
            if res == 1:
                ans = tmp

    for i in range(N):
        for j in range(N-M+1):
            tmp = ''
            for k in range(j, j+M):
                tmp += arr[k][i]
            res = same(tmp)
            if res == 1:
                ans = tmp

    print('#{} {}'.format(t, ans))

