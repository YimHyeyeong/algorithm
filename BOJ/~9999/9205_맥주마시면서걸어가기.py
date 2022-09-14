from sys import stdin
from collections import deque

def func(x,y):
    q = deque()
    q.append((x,y)) # 집 위치 담아주기
    while q:
        r,c = q.popleft()
        if abs(festival[0] - r) + abs(festival[1] - c) <= 1000: # 현재 위치와 페스티벌까지의 거리가 1000 이하인 경우
            print("happy") # 페스티벌까지 도착할 수 있음
            return

        for i in range(n): 
            if not visited[i]: # 방문하지 않은 편의점인 경우
                nr, nc = store[i]
                if abs(r - nr) + abs(c - nc) <= 1000: # 1000m안에 들어와서 편의점까지 갈 수 있는 경우
                    q.append((nr,nc))
                    visited[i] = 1 # 방문표시

    print("sad")
    return
T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline().strip())
    home = list(map(int, stdin.readline().split())) # 집 위치 저장
    store = [list(map(int,stdin.readline().strip().split())) for _ in range(n)] # 편의점들의 위치 저장
    festival = list(map(int,stdin.readline().strip().split())) # 페스티벌 위치 저장
    visited = [0] * n # 방문 표시
    func(home[0], home[1])
