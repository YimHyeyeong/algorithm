#[1] 다익스트라 문제
import heapq
import sys
V,E = map(int,input().split()) # V:정점 개수 / E:간선 개수
K = int(input()) # 시작위치
adj = [[] for _ in range(V+1)]  # 경로와 가중치 저장
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())   # 여러 줄로 input받을때 readline()안하니 시간초과뜸
    adj[u].append((w,v))

min_heap =[]
heapq.heappush(min_heap,(0,K)) # 시작 위치와 가중치 저장
dist = [int(21e8) for _ in range(V+1)]  # 가중치 저장
while min_heap:
    cost,now = heapq.heappop(min_heap)
    if dist[now] != int(21e8) : continue # 21e8이 아니라면 이미 최단 경로가 저장된 것.
    dist[now] = cost

    for w,n in adj[now]:
        heapq.heappush(min_heap,(cost+w,n))

for i in range(1,V+1):
    if dist[i] == int(21e8):  # 경로가 없는 경우
        print('INF')
    else:
        print(dist[i])