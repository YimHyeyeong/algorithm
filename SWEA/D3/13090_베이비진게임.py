def func(p):
    for j in range(10):
        if p[j] >= 3:
            return True
        if p[j] and p[j+1] and p[j+2] :
            return True
    return False


tc = int(input())
for t in range(1,tc+1):
    lst = list(map(int,input().split()))
    p1 = [0 for _ in range(12)]  # 인덱스 에러 방지를 위해 12
    p2 = [0 for _ in range(12)]
    res = 0
    for i in range(0, 12, 2):
        p1[lst[i]] += 1  # 짝수
        p2[lst[i+1]] += 1 # 홀수 

    if func(p1): # p1이 먼저 승리시
        res = 1
    if func(p2): # p2가 먼저 승리시
        res = 2

    print('#{} {}'.format(t,res))