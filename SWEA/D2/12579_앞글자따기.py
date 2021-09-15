T = int(input())

for i in range(1, T + 1):

    N = int(input())

    st = input().split()

    w = ''
    for j in range(N):
        w += st[j][0].upper()

    print('#{} {}'.format(i, w))