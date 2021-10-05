#[1]
tc= int(input())

for t in range(1, tc+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    lst.sort(key = lambda x : x[1])  # 람다를 이용해 리스트의 2번째 값(=끝나는 시간)을 기준으로 오름차순 정렬

    cnt = 0
    res = 0  # 끝나는 시간 저장 
    for i in range(N):
        if lst[i][0] >= res: # 끝나는 시간보다 다음 시작 시간이 같거나 더 뒤에 시작하거나
            res = lst[i][1]  # 뒤의 값의 끝나는 시간 저장
            cnt += 1  

    print('#{} {}'.format(t, cnt))

############
[2]

class schedule :
    def __init__(self, a,b):
        self.start = a
        self.end = b

def cmp(s_var):
    #s_var.start, s_var.end
    return (s_var.end,s_var.start) # end 시간 기준으로 오름차순 정렬

T = int (input())

for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N) :
        a,b = map(int, input().split())
        lst.append(schedule(a,b))

    # end 시간 기준으로 정렬하기
    lst.sort(key = cmp)
    
    cnt = 0
    now = 0

    # end시간이 빠른순서대로 선택이 된다 (정렬을 해놨으니까) -> 그리디
    for i in range(len(lst)) :
        # now < schedule.start
        if now <= lst[i].start :
            cnt += 1
            now = lst[i].end # now 갱신

    print("#{} {}".format(tc, cnt))