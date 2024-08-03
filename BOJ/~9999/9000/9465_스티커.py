from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    arr = [list(map(int,stdin.readline().split())) for _ in range(2)]

    for i in range(1,n):
        if i == 1: # 런타임 에러 조심
            arr[0][1] += arr[1][0]
            arr[1][1] += arr[0][0]
        else:
             # 점화식 생각해보길.. i에 올 수 있는 겅우는 다른 줄의 i-1, i-2 번째에서 오는 경우밖에 없음 
            arr[0][i] += max(arr[1][i-1], arr[1][i-2]) # 그 중에서 가장 큰 값을 골라 저장하기
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])

    print(max(arr[0][n-1],arr[1][n-1]))
