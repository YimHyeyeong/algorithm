from sys import stdin
from collections import deque

def func(n):
     q = deque()
     q.append(n)
     visited[n] = 1 
     while q:
        t = q.popleft()
        if t == K:
            return visited[t]
        for i in (t-1, t+1, t*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[t] +1 
                q.append(i)


N,K = map(int, stdin.readline().split())
visited = [0] * 100001 # N,K가 0보다 크고 100000보다 작은 숫자이기 때문
print(func(N)-1)  # 함수 처음에 visited[n] =1 을 해줘서 -1해야함. 처음 시작부터 1초는 아니니까..
