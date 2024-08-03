N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0
for i in range(N-1,-1,-1):  # 큰 값부터 차례로 나눔
    cnt += K//lst[i]  # 몫을 cnt에 저장
    K = K%lst[i]  # 나머지 값을 다시 K에 저장

print(cnt)