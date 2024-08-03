import heapq
from sys import stdin
# 최소힙
N = int(stdin.readline())
heap = []
for _ in range(N):
    i = int(stdin.readline())
    if i:
        heapq.heappush(heap,i)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)