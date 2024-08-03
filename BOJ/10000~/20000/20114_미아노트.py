from sys import stdin

def func(n):
    global res
    for i in range(W*n, W*(n+1)): # 다음 문자열까지 탐색
        for j in range(H):
            if arr[j][i] != '?':
                res += arr[j][i]
                return
    res += '?'
    return
N , H, W = map(int, stdin.readline().split())

arr = [list(stdin.readline().strip()) for _ in range(H)]
res = ''

for k in range(N):
    func(k)


print(res)
