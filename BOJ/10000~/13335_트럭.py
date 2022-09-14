from sys import stdin
from collections import deque # 먼저 온 트럭이 먼저 가야하니까 (선입선출) 큐 사용

n,w,L = map(int,stdin.readline().split())

lst = deque(map(int,stdin.readline().split()))

res = [0] * w  # 다리 길이
res = deque(res)

time = 0

while res:  #반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복
    time += 1
    res.popleft() # 다리의 칸을 하나씩 줄인다.

    # 모든 트럭을 확인
    if lst:
        # 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가
        # 다리의 하중보다 크다면 빈 공간을 추가
        if sum(res) + lst[0] > L:
            res.append(0)
        # 다리의 하중보다 작다면 트럭을 다리에 추가
        else:
            res.append(lst.popleft())

print(time)


