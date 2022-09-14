from sys import stdin

visited = []
res = 'Valid'
for i in range(36):
    a = stdin.readline().rstrip()
    r = int(a[1])
    c = ord(a[0])
    if i == 0: # 처음 위치 저장
        start_r, start_c = r,c
        pre_r, pre_c = start_r, start_c
        visited.append((start_r, start_c)) # 방문 표시
        continue
    elif i < 35:
        if abs(pre_r-r) == 2 and abs(pre_c-c) ==1 or abs(pre_r-r) == 1 and abs(pre_c-c) ==2 and (r,c) not in visited:
            visited.append((r,c))
            pre_r, pre_c = r, c # 현재 위치를 이전 값으로 바꿈
        else:
            res = 'Invalid'
            break

    else:
        if abs(r-start_r) == 2 and abs(c-start_c) ==1 or abs(r-start_r) == 1 and abs(c-start_c) ==2 and (r,c) not in visited:
            pass
        else:
            res = 'Invalid'

print(res)



