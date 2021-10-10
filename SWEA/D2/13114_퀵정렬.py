
def P(A,l,r):
    p = A[l]  # 제일 앞에꺼가 피봇이 됨
    i,j = l,r
    while i <= j:
        while i <= j and A[i] <= p:  # 피봇보다 큰거 찾기
            i += 1
        while i <= j and A[j] >=p:  # 피봇보다 작은거 찾기
            j -= 1
        if i < j:  
            A[i], A[j] = A[j],A[i]  # 큰 것과 작은 거 교환
    A[l], A[j] = A[j], A[l]  # while문이 다 돌면 j가 i보다 작아짐 -> j위치에 있는 것과 교환하면 j위치를 기준으로 피봇보다 작은것과 큰게 나눠짐
    return j  # 피봇의 위치가 j가 됨

def Q(A, l, r):
    if l<r:
        s = P(A,l,r)
        Q(A,l,s-1) # 리턴된 피봇을 기준으로 나눠서 다시 정렬
        Q(A,s+1,r)


tc = int(input())

for t in range(1,tc+1):
    N = int(input())
    lst = list(map(int, input().split()))
    Q(lst, 0, N-1)

    print('#{} {}'.format(t,lst[N//2]))