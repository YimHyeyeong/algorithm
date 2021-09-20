tc = int(input())

for t in range(1, tc +1):

    N = int(input())

    lst = list(map(int,input()))

    lst_1 = [0] * 10
    for i in lst:
        lst_1[i] += 1

    idx = max_num = 0

    for j in range(9,-1,-1):
        if lst_1[j] > max_num:
            max_num = lst_1[j]
            idx = j

    print('#{} {} {}'.format(t,idx,max_num))