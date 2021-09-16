def inorder(idx):
    if idx > N:
        return
    if (idx * 2) <= N:
        inorder(idx * 2)
    ans.append(node[idx])
    if (idx *2 + 1) <= N:
        inorder(idx * 2 + 1)

for tc in range(10):
    N = int(input())
    node = [0] * (N+1)
    for n in range(N):
        vals = list(input().split())
        node[int(vals[0])] = vals[1]
    ans = []
    inorder(1)
    print("#{} {}".format(tc +1, ''.join(ans)))