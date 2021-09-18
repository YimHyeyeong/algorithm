tc = int(input())

for t in range(1, tc + 1):
    n = int(input())

    lst = list(map(int,input().split()))

    m_ax = 0

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if  lst[i] > lst[j]:
                cnt += 1

        if cnt > m_ax:
            m_ax = cnt

    print('#{} {}'.format(t,m_ax))