tc = int(input())

for t in range(1, tc +1):
    N,Q = map(int,input().split())



    lst = [0] * N

    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for j in range(L-1,R):
            lst[j] = i
    print('#{}'.format(t), end = ' ')
    print(*lst)




