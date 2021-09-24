def order(n):
    if n:
        print(n, end=' ')  # 전위순회, 정점번호를 출력
        order(left[n])
        order(right[n])

tc = int(input())

for t in range(1,tc+1):
    V = int(input())

    left = [0] *(V+1)
    right = [0] * (V+1)

    for i in range(V-1):
        p, c = map(int,input().split())
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    print('#{}'.format(t), end=' ')
    order(1)
    print()


