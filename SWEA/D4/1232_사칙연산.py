
def func(idx):
    if idx > N: return    # 인덱스 초과 시 리턴 
    if type(tree[idx]) == int:   # 단말노드일 경우
        return tree[idx]          # 피연산자 리턴

    a = func(left[idx])     # 왼쪽 트리
    b = func(right[idx])     # 오른쪽  트리 

    if tree[idx] == '+':
        return a + b

    elif tree[idx] == '-':
        return a - b

    elif tree[idx] == '*':
        return a * b
        
    elif tree[idx] == '/':
        return a / b


tc = 10

for t in range(1, tc+1):

    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)  # 왼쪽 트리
    right = [0] * (N+1)  # 오른쪽 트리

    for i in range(N):
        lst = input().split()

        if len(lst) > 2:   # 연산자가 있는 경우
            tree[int(lst[0])] = lst[1]    
            left[int(lst[0])] = int(lst[2])
            right[int(lst[0])] = int(lst[3])


        else:
            tree[int(lst[0])] = int(lst[1])  # 리프 노드인 경우

    res = int(func(1))
    print('#{} {}'.format(t,res))
