def Union(a,b):
    global cnt
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        cnt -= 1  # Union 할때마다 전체 개수에서 1빼기
        parents[pb] = pa
    return

def Find(x):
    if parents[x] == x : return x
    ret = Find(parents[x])
    parents[x] = ret
    return ret

tc = int(input())
for t in range(1,tc+1):
    N,M = map(int,input().split())
    lst= list(map(int,input().split()))
    parents = [i for i in range(N+1)]
    cnt = N
    for j in range(M):
        Union(lst[j*2],lst[j*2+1])

    print('#{} {}'.format(t,cnt))
