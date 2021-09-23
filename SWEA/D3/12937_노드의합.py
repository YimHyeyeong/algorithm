def dfs(idx):
    if idx > N: return # 노드의 개수 초과시 return
    dfs(idx * 2) # 왼쪽 트리
    dfs(idx * 2 + 1)  # 오른쪽 트리
    if tree[idx] ==0 :  # 리프노드가 아니면 자식 노드들의 합 넣기
        tree[idx] = tree[idx * 2] + tree[idx * 2 +1]


tc = int(input())

for t in range(1, tc+1):
    N, M, L = map(int,input().split()) # 노드의 개수, 리프노드의 개수, 값을 출력할 노드 번호

    tree = [0 for _ in range(N+2)]  # 리프노드가 하나만 있는 경우를 대비해서 +1이 아니라 +2
    for i in range(M):
        A, B = map(int, input().split())
        tree[A] = B

    dfs(L)  # L까지만 구하면 되니까
    print('#{} {}'.format(t, tree[L]))

