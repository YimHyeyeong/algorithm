#[1]
def mergeSort(s, e):
    # 재귀호출을 할 것인가?, 기저사례인가?
    if s + 1 == e:  # e를 N으로 잡았기 때문에 +1이 e일때 리턴
        return
    # 분할 하자구~~
    mid = (s + e) // 2
    mergeSort(s, mid) # s ~ mid-1까지 고려하기 때문에
    mergeSort(mid, e) # mid + 1 안함 mid ~ e-1 / 문제에서 N//2를 기준으로 나눴기 때문에
    # 카운팅
    if arr[mid - 1] > arr[e - 1]: 
        global cnt; cnt += 1

    # 병합하는 작업
    i, j, k = s, mid, s
    while i < mid and j < e: # 등호없음 , 당연함 e가 N이니까,,
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]; j, k = j + 1, k + 1
    while i < mid:
        tmp[k] = arr[i]; i, k = i + 1, k + 1
    while j < e:
        tmp[k] = arr[j]; j, k = j + 1, k + 1
    for i in range(s, e):
        arr[i] = tmp[i]


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    mergeSort(0, N)  # 인덱스보다 하나 더 많음
    print('#{} {} {}'.format(tc, arr[N//2], cnt))



########################
#[2]
def merge(ls,le,rs,re):
    global cnt
    if lst[le] > lst[re] : cnt += 1
    res = [0] * (re-ls+1)
    a = ls
    b = rs
    t = 0
    #left[a] vs right[b] -> res 넣기
    while a <= le and b <= re :
        if lst[a] <= lst[b] :
            res[t] = lst[a]
            a += 1
            t += 1
        elif lst[b] < lst[a] :
            res[t] = lst[b]
            b += 1
            t += 1
    while a <= le :
        res[t] = lst[a]
        a += 1
        t += 1
    while b <= re :
        res[t] = lst[b]
        b += 1
        t += 1
    # res -> lst
    t = 0
    for i in range(ls,re + 1) :
        lst[i] = res[t]
        t += 1

def merge_sort(s,e):
    if s == e : return # 1개짜리는 정렬 완료
    mid = (s + e-1) // 2  # 문제에서 N//2로 슬라이싱해서 -1해줘야 맞음
    merge_sort(s,mid) # left 정렬되어있다. [s~mid]
    merge_sort(mid+1,e) # right 정렬되어있다.[mid+1~e]
    merge(s,mid,mid+1,e)

    return

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    merge_sort(0,len(lst)-1) #e를 마지막 인덱스로 둠

    print("#{} {} {}".format(tc, lst[N//2], cnt))