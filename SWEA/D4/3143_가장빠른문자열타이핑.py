
def same(idx, num):
    if idx + num - 1 >= len(A):
        return 0

    for k in range(num):
        if A[idx + k] != B[k]:
            return 0

    return 1

tc = int(input())

for t in range(1, tc+1):

    A, B = input().rstrip().split()

    cnt = 0
    i = 0
    n = len(A)

    while i < n:
        res = same(i, len(B))

        if res == 1:
            cnt += 1
            i += len(B)
        else:
            cnt += 1
            i += 1

    print('#{} {}'.format(t, cnt))
