N, M = map(int, input().split())

arr = [input() for _ in range(N)]
check = []
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i ,i+8):
            for q in range(j, j+8): # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (k+q) % 2 ==0:
                    if arr[k][q] !='W': cnt1 += 1
                    if arr[k][q] !='B': cnt2 += 1
                else:
                    if arr[k][q] != 'B': cnt1 += 1
                    if arr[k][q] != 'W': cnt2 += 1

        check.append(cnt1)   # W로 시작했을 때 칠해야 할 부분
        check.append(cnt2)   # B로 시작했을 때 칠해야 할 부분
print(min(check))