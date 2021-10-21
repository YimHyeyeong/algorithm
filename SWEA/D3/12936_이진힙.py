tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    lst = list(map(int,input().split()))

    tree = [0]
    for i in range(len(lst)):
        tree.append(lst[i])

        now = len(tree) -1
        par = now // 2

        while now > 1 and tree[par] > tree[now]:
            tree[par], tree[now] = tree[now], tree[par]
            now = par
            par = now // 2


    total = 0
    k = N
    while k:
        k //= 2
        total += tree[k]

    print('#{} {}'.format(t, total))