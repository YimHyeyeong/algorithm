N = int(input())
tree = {}
for _ in range(N):
    a,b,c = input().split()
    tree[a] = [b,c]

preorder = []
inorder = []
postorder = []

def func(now):
    if now == '.': return  # 없으면 리턴
    preorder.append(now)
    func(tree[now][0])   # 왼쪽
    inorder.append(now)
    func(tree[now][1])   # 오른쪽
    postorder.append(now)
    return

func('A')
print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))



