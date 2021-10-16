import heapq

def dij(s):
    minheap = []
    dist = [int(21e8) for _ in range(N+1)]
    heapq.heappush(minheap,(0,s))
    while minheap:
        cost, now = heapq.heappop(minheap)
        if dist[now] != int(21e8) : continue
        dist[now] = cost
        for w,next in adj[now]:
            heapq.heappush(minheap,(cost+w,next))
    return dist


tc = int(input())
for t in range(1,tc+1):
    N,E = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        adj[s].append((w,e))

    dist = dij(0)
    print('#{} {}'.format(t,dist[N]))