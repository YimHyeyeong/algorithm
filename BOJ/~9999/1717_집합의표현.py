def Union(a,b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        parents[pb] = pa
    return

def Find(x):
    if parents[x] == x : return x

    ret = Find(parents[x])
    parents[x] = ret
    return ret


N,M = map(int,input().split())
parents = [i for i in range(N+1)]
res = []  # 이거 안하니 시간초과나옴,,
for _ in range(M):
    cmd,a,b = map(int,input().split())
    if cmd == 0:
        Union(a,b)
    else:
        if Find(a) == Find(b):
            res.append('YES\n')
        else:
            res.append('NO\n')

print('{}'.format(''.join(res)))