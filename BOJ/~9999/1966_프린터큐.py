from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx_que = deque(list(range(N)))  # q[M]이 어디있는지 알기위해
    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1  # 우선 순위가 가장 높은 것 출력
            q.popleft()
            if idx_que.popleft() == M:  # M이 출력될 차례
                print(cnt)
        else:
            q.append(q.popleft()) # 가장 큰 수가 아니라면 뒤로 보내기
            idx_que.append(idx_que.popleft())

