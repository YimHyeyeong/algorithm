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
        if c == 2 or c == 0:   # 처음이거나 이전에 반대쪽에 있었을경우
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
#[2]

def binary_search(s,e, target):
    flag = 0 # 'left' ,'right' 이전상태
    while s <= e :
        mid = (s + e) // 2
        if A[mid] == target :
            return True
        elif target < A[mid] :
            if flag == 0 : flag = 'right'
            elif flag == 'right' : return False
            flag = 'right'
            e = mid - 1 # s  mid target  e   right 구간선택함
        elif A[mid] < target :
            if flag == 0 : flag = 'left'
            elif flag == 'left' : return False
            flag = 'left'
            s = mid + 1 # s target  mid   e    left 구간선택

    return False


T = int(input())

for tc in range(1, T + 1) :
    N,M = map(int, input().split()) # N : A의 크기 , M : B 의 크기
    A = list(map(int ,input().split()))
    B = list(map(int ,input().split()))
    A.sort()
    cnt = 0
    for i in range(len(B)):
        target = B[i]
        ret = binary_search(0,len(A)-1, target) # 존재하고 + 번갈아가면서 탐색되는지
        if ret == True:
            cnt += 1
    print("#{} {}".format(tc, cnt))