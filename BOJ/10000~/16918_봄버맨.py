from sys import stdin

R,C,N = map(int, stdin.readline().split())

arr = [stdin.readline().rstrip() for _ in range(R)]

if N <= 1:
    for i in arr:
        print(i)

elif N % 2 == 0:  # 짝수일 때는 무조건 채워지는 타임
    for _ in range(R):
        print('O' * C)

else:
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    arr1 = [[0] * C for _ in range(R)]  # 첫번째로 터지는 구간
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 'O':
                arr1[r][c] = '.'
                for q in range(4):
                    nr = r + dr[q]
                    nc = c + dc[q]
                    if 0 <= nr < R and 0 <= nc < C:
                        arr1[nr][nc] = '.'
            elif arr[r][c] == '.' and arr1[r][c] != '.':
                arr1[r][c] = 'O'

    arr2 = [[0] * C for _ in range(R)]  # 두번째로 터지는 구간
    for r in range(R):
        for c in range(C):
            if arr1[r][c] == 'O':  # 폭탄 상하좌우 처리
                arr2[r][c] = '.'
                for q in range(4):
                    nr = r + dr[q]
                    nc = c + dc[q]
                    if 0 <= nr < R and 0 <= nc < C:
                        arr2[nr][nc] = '.'
            elif arr1[r][c] == '.' and arr2[r][c] != '.':
                arr2[r][c] = 'O'


    if N % 4 == 3:
        for w in arr1: print(''.join(w))
    elif N % 4 == 1:
        for w in arr2: print(''.join(w))



