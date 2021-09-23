# [1]
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


############################################

# [2]
def dfs(idx) :
    if idx > N : return
    if tree[idx] > 0 : return
    dfs(idx * 2) # left subtree 값 채우기
    dfs(idx * 2 + 1) # right subtree 값 채우기

    # tree[idx]= tree[idx * 2 ] + tree[idx * 2 + 1]
    if idx * 2 <= N : tree[idx] += tree[idx * 2]    # 인덱스 에러 방지
    if idx * 2 + 1 <= N : tree[idx] += tree[idx * 2 + 1]  # 인덱스 에러 방지



# [3]
T = int(input())

def dfs(idx) :
    if idx > N : return 0
    if tree[idx] > 0 : return tree[idx]
    a = dfs(idx * 2) # left subtree 값 채우기
    b = dfs(idx * 2 + 1) # right subtree 값 채우기
    tree[idx] = a + b
    return tree[idx]  


for tc in range(1, T + 1) :
    N,M,L = map(int, input().split())
    tree = [0] * (N + 1)     # dfs에서 인덱스 방지했기 때문에 +1해도 됨
    for i in range(M):
        a,b = map(int, input().split())
        tree[a] = b

    dfs(1)
    print("#{} {}".format(tc, tree[L]))



####################
# [4] DP로 풀기

T = int(input())

for tc in range(1, T + 1) :
    N,M,L = map(int, input().split())
    dp = [0] * ( N + 1 )
    num = int(21e8)
    for i in range(M):
        a,b = map(int, input().split())
        dp[a] = b
        num = min(num, a)

    for i in range(num - 1, 1-1, -1):
        if i * 2 + 1 <= N :
            dp[i] = dp[i * 2] + dp[i * 2 + 1]
        else :
            dp[i] = dp[i * 2]
    print("#{} {}".format(tc, dp[L]))