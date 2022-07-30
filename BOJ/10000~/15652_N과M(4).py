#[1]
def f(level,start):

    if level == M:
        for j in range(M):
            print(p[j], end=' ')
        print()
        return
    # 선택 후 재귀호출    
    for i in range(start, N+1):  # 이전의 레벨의 수보다 같거나 커야하니까
        p[level] = i
        f(level+1, i)
        p[level] = 0


N,M = map(int,input().split())  # N 개가지 , M개를 선택(M레벨의 깊이)
p = [0] *8
f(0,1)




#####################
[2]

def f(level):
    if level == M:
        for j in range(M):
            print(p[j], end=' ')
        print()
        return


    if level == 0:   # 0의 단계에서는 아무 숫자가 와도 됨
        for i in range(1, N+1):
            p[level] = i
            f(level+1)
            p[level] = 0
    else:
        for j in range(p[level-1], N+1):   # 0이후의 단계에서는 바로 앞의 단계 수보다 크거나 같아야 함
            p[level] = j
            f(level +1)
            p[level] = 0


N,M = map(int,input().split())
p = [0] *8
f(0)
