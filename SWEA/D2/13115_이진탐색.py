#[1] 재귀
def search(l,r,t,c):
    global res
    if l > r:
        return

    mid = (l+r) // 2

    if t == A[mid]:
        res += 1
        return

    elif t > A[mid]:
        if c == 2 or c == 0:
            search(mid+1,r,t,1)
    else:
        if c == 1 or c == 0:
            search(l,mid-1,t,2)

tc= int(input())

for t in range(1,tc+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    res = 0
    for i in range(M):
        b = B[i]
        search(0, len(A)-1, b, 0)
    print('#{} {}'.format(t,res))




####
#[2] 반복
def search(key):
    l = 0
    r = N-1
    d = -1
    while l <= r:
        mid = (l+r) // 2
        if key == A[mid]:
            return 1
        elif key < A[mid]:
            if d == 0 : return 0 
            r = mid -1
            d = 0
        else:
            if d == 1 : return 0
            l = mid + 1
            d = 1
    return 0 