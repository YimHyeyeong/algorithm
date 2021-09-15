for i in range(1, 11):

    t= int(input())
    tc = list(map(int,input().split()))
    cnt = 0
    idx = 2

    while idx < t-2:
        if tc[idx] <= tc[idx-2] or tc[idx] <= tc[idx-1] or tc[idx] <= tc[idx+1] or tc[idx] <= tc[idx+2]:
            idx += 1

        else:
            cnt += tc[idx] - max(tc[idx-2], tc[idx-1], tc[idx+ 2], tc[idx+1])
            idx += 3

    print('#{} {}'.format(i, cnt))

