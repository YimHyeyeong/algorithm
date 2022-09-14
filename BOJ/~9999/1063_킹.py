from sys import stdin

king, stone, N = stdin.readline().split()
lst = list(stdin.readline().rstrip() for _ in range(int(N)))

start_king = [8-int(king[1]), ord(king[0]) - 65] # 숫자로 변환
start_stone = [8-int(stone[1]), ord(stone[0]) - 65]

dir = {
    "R": (0,1),
    "L":(0,-1),
    "B": (1,0),
    "T": (-1,0),
    "RT": (-1,1),
    "LT": (-1,-1),
    "RB" : (1,1),
    "LB": (1,-1)
}

for i in lst:
    dr, dc = dir[i]
    k_nr = start_king[0] + dr # 킹의 새로운 위치
    k_nc = start_king[1] + dc
    
    # 체스판 넘어가면 그냥 건너뛰기
    if 0 <= k_nr < 8 and 0 <= k_nc < 8:
        # 이동한 곳이 돌과 같은 위치라면
        if [k_nr, k_nc] == start_stone:
            # 돌도 같은 방향으로 이동시키기
            s_nr = start_stone[0] + dr
            s_nc = start_stone[1] + dc
            if 0 <= s_nr < 8 and 0 <= s_nc < 8:
                start_king = [k_nr, k_nc]
                start_stone = [s_nr, s_nc]

        else:
            start_king = [k_nr, k_nc]

print(chr(start_king[1]+65)+str(8-start_king[0]))
print(chr(start_stone[1]+65)+str(8-start_stone[0]))
