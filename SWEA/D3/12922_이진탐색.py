def f(now):
    global cnt
    if now > N:  # 초과하면  리턴
        return
    f(now * 2)  # 왼쪽 트리
    tree[now] = cnt
    cnt += 1
    f(now * 2 + 1) # 오른쪽 트리


tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]  # 노드번호를 이용해서 출력해야 하니까 ? 인접리스트로하려면 어려움
    cnt = 1   # 1~N까지 차례로 밑에서 넣으면 됨, 중위순회로

    f(1)
    print('#{} {} {}'.format(t, tree[1], tree[N//2]))