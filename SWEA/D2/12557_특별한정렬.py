tc = int(input())

for t in range(1, tc+1):
    n = int(input())

    lst = list(map(int,input().split()))

    def bsort(a):
        for i in range(len(a)-1,0,-1):
            for j in range(i):
                if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1], a[j]
        return a

    lst = bsort(lst)

    res = []

    for i in range(5):
        res.append(lst[n-1-i])

        res.append(lst[i])


    print('#{}'.format(t), *res)
    