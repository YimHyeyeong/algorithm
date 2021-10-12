tc = int(input())

for t in range(1, tc +1):
    p, a, b = map(int, input().split())

    def search(k, key):
        start = 1
        end = k
        cnt = 0
        while start <= end:
            cnt += 1
            mid = (start + end) // 2
            if mid == key:
                return cnt
            elif mid > key:
                end = mid
            else:
                start = mid



    print('#{}'.format(t), end=' ')
    res_a = search(p,a)
    res_b = search(p,b)
    if res_a > res_b:
        print('B')
    elif res_a < res_b:
        print('A')
    else:
        print(0)
