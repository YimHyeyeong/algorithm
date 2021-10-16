#[1] 크루스칼 알고리즘
def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        parents[pb] = pa
    return

def Find(x):
    if parents[x] == x: return x
    ret = Find(parents[x])
    parents[x] = ret
    return ret

tc = int(input())
for t in range(1,tc+1):
    V,E = map(int,input().split())
    edge_list = [list(map(int,input().split())) for _ in range(E)]
    edge_list.sort(key=lambda x:x[2])  # 가중치를 기준으로 오름차순
    parents = [i for i in range(V+1)]
    total = 0
    for edge in edge_list:
        if Find(edge[0]) != Find(edge[1]):
            total += edge[2]  # 가중치 더하기
            Union(Find(edge[0]), Find(edge[1]))

    print('#{} {}'.format(t,total))

