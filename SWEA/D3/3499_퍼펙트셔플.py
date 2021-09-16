tc = int(input())

for t in range(1, tc +1):
    n = int(input())
    lst = list(input().split())

    i = 0
    j = (n+1) // 2

    print(f'#{t}', end = ' ')

    for k in range(n//2):
        print(lst[i+k], end = ' ')
        print(lst[j+k], end = ' ')

    if n % 2:
        print(lst[n//2])
    else:
        print()