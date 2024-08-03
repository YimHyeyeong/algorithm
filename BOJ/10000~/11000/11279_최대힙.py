import heapq 
from sys import stdin # 안하면 시간초과

N = int(stdin.readline())
heap = []
for _ in range(N):
    t = int(stdin.readline())
    if t:
        heapq.heappush(heap,(-t, t))  # heapq 모듈은 최소 힙만 지원함
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
