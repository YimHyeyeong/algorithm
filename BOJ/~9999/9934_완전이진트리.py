from sys import stdin

def func(arr, n):
    mid = len(arr) // 2 # arr[mid]가 부모 노드
    res[n].append(arr[mid])
    if len(arr) ==1:
        return
    func(arr[:mid], n+1)
    func(arr[mid+1:], n+1)


K = int(stdin.readline())

lst = list(map(int, stdin.readline().split()))

res = [[] for _ in range(K)]

func(lst, 0)
for i in res:
    print(*i)
