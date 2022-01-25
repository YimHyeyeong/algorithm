def func(start, cnt):
    if cnt == M:
        print(*lst)

    else:
        for i in range(start, N+1):
            if used[i]: continue
            used[i] = 1
            lst[cnt] = i
            func(i+1, cnt+1)
            used[i] = 0




N, M = map(int, input().split())
used = [0] * 9
lst = [0] * M
func(1,0)