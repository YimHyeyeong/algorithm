import heapq
from sys import stdin

N = int(stdin.readline())
heap = []
for _ in range(N):
    i = int(stdin.readline())
    if i != 0:
        heapq.heappush(heap,(abs(i), i))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)