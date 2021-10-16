import heapq
ugly =[0] * 1501 # 1~1500
min_heap = []
th = 1
heapq.heappush(min_heap,1) # 1을 먼저 push
p = -1
while th < 1501:
    now = heapq.heappop(min_heap)
    if p == now : continue  # 중복되는 것이 있다면 ugly에 저장하지 x

    ugly[th] = now
    th += 1

    heapq.heappush(min_heap,now*2)
    heapq.heappush(min_heap,now*3)
    heapq.heappush(min_heap,now*5)
    p = now


tc = int(input())
for t in range(1,tc+1):
    N = int(input())
    lst = list(map(int,input().split()))
    print('#{}'.format(t), end=' ')
    for i in lst:
        print(ugly[i], end=' ')
    print()


