for i in range(1, 11):

    t = int(input())

    lst = list(map(int, input().split()))

    while t:
        max_lst = max(lst)
        min_lst = min(lst)
        max_idx = lst.index(max(lst))
        min_idx = lst.index(min(lst))

        lst[max_idx] -= 1
        lst[min_idx] += 1

        t -= 1

    print('#{} {}'.format(i, max(lst)-min(lst)))