tc = int(input())
for i in range(1, tc+1):

    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_num = 0
    for j in range(0,M):
        sum_num += lst[j]
        
    max_num = min_num = sum_num
    for k in range(M,N):
        sum_num = sum_num - lst[k - M] + lst[k]
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < min_num:
            min_num = sum_num

    res = max_num - min_num

    print('#{} {}'.format(i, res))
