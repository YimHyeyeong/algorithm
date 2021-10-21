def f(n):
    global cnt
    if n :
        cnt += 1
        f(left[n])
        f(right[n])



tc = int(input())

for t in range(1, tc+1):
    E, N = map(int, input().split())

    edge = list(map(int,input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    cnt = 0
    for i in range(E):
        p,c = edge[i*2], edge[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    f(N)
    print('#{} {}'.format(t,cnt))