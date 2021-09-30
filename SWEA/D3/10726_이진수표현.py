tc = int(input())

for t in range(1, tc+1):
    N, M = map(int,input().split())
    print('#{}'.format(t), end=' ')

    new_M = M & ((1<<N) -1)    # N개의 비트만 뽑아서 new_M에 저장

    if (1 << N) -1 == new_M:   # N개의 1로 이루어진 비트와 비교했을 때 같을 경우 on
        print('ON')

    else:
        print('OFF')

