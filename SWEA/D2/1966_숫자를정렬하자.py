tc = int(input())

for t in range(1, tc+1):
    n = int(input())

    lst = list(map(int,input().split()))

    for i in range(n-1,0,-1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    print('#{}'.format(t), end= ' ')
    
    print(*lst)