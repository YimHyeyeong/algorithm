from collections import deque
N, M = map(int, input().split())

q = deque(list(map(int,input().split()))) # 뽑고 싶은 덱
idx_q = deque(list(range(1,N+1))) # 숫자를 뽑아낼 덱
cnt = 0

for i in q:
    while True:
        if idx_q[0] == i:  # 1번 연산
            idx_q.popleft()
            break
        if idx_q.index(i) - 0 <= len(idx_q) - idx_q.index(i): # 2번 연산
            idx_q.append(idx_q.popleft())
            cnt += 1
        else: # 3번 연산
            idx_q.appendleft(idx_q.pop())
            cnt += 1
print(cnt)
