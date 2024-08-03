from sys import stdin

N, K = map(int, stdin.readline().split())

lst = list(map(int, stdin.readline().split()))

cns = 0

for i in range(N-1, 0 ,-1): #뒤에서 부터
    max_idx = lst.index(max(lst[:i]))
    if lst[i] < lst[max_idx]:
        lst[i], lst[max_idx] = lst[max_idx] , lst[i]
        cns +=1
        if cns == K:
            print(lst[max_idx], lst[i])
            break
if cns < K:
    print(-1)