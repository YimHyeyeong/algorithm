import heapq  # 최소힙이 기본
from sys import stdin

N = int(stdin.readline())

leftheap = [] # 최대힙
rightheap = [] # 최소힙

for _ in range(N):
    i = int(stdin.readline())
    # heap들의 길이가 같다면 중간값의 기준이 되는 leftheap에 넣는다. 
    if len(leftheap) == len(rightheap): # 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다. -> 중간값이 leftheap에 있어야 함
        heapq.heappush(leftheap, (-i, i))
    else: # 길이가 다르다면 맞추기 위해 rightheap에 넣는다
        heapq.heappush(rightheap, (i, i))

    # left의 루트가right루트보다 크면 루트를 서로 바꾼다
    if rightheap and leftheap[0][1] > rightheap[0][1]:
        leftvalue = heapq.heappop(leftheap)[1]
        rightvalue = heapq.heappop(rightheap)[1]
        heapq.heappush(leftheap, (-rightvalue, rightvalue))
        heapq.heappush(rightheap, (leftvalue,leftvalue))

    print(leftheap[0][1])