N, S = map(int,input().split())
lst = list(map(int,input().split()))

def func(idx, sum):
    global cnt
    if idx == N: # N-1하면 안됨..0,1,2,...N-1 -> 총 N개 선택
        if sum == S:
            cnt += 1

        return

    func(idx +1, sum+lst[idx])  # 선택 후 재귀호출
    func(idx+1, sum) # 안선택 후 재귀 호출

cnt = 0
func(0,0)
if S == 0:  # 공집합제거
    cnt -= 1

print(cnt)