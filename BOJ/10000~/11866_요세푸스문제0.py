
N, K = map(int, input().split())
q = []
lst = []
num = K -1
for i in range(1,N+1):
    q.append(i)

for _ in range(N):
    if len(q) > num: # 한 바퀴 돌기전
        lst.append(q.pop(num))
        num += K -1
    else: # 한 바퀴 돈 후
        num = num % len(q)
        lst.append((q.pop(num)))
        num += K -1

print('<',', '.join(str(i) for i in lst),'>', sep = '')

