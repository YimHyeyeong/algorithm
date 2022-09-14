from sys import stdin

def func(cnt):  # 장애물을 놓는 함수
    global res, teacher

    if cnt == 3: # 장애물 3개를 모두 다 놓았을 경우
        M = 0
        for k in range(N):
            for q in range(N):
                if arr[k][q] == 'T': # 선생이 볼 수 있는지 없는지 확인
                    if check(k,q): # k,q 에 있는 선생이 볼 수 있는 학생이 없는 경우
                        M += 1  # 아무 학생도 볼 수 없는 선생의 수 추가
                    else: # 한명이라도 학생을 볼 수 있는 경우 cnt 2로 리턴
                        return

        if M == teacher:  #  모든 선생이 아무 학생도 볼 수 없는 경우
            res = True
        return

    for i in range(N): # 모든 칸에 장애물을 놓아보기
        for j in range(N):
            if arr[i][j] == 'X' :
                arr[i][j] = 'O'
                func(cnt + 1)
                arr[i][j] = 'X'


dr = [-1,1,0,0]
dc = [0,0,-1,1]
def check(x,y):  # 선생이 학생을 볼 수 있는지 없는지 확인하는 함수
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 'O': # 한칸만 움직이는 것이 아닌 같은 방향으로 쭉 가야함
            if arr[nr][nc] == 'S': # 학생을 볼 수 있는 경우
                return False 
            else: # 아니라면 계속 진행
                nr += dr[i]
                nc += dc[i]
    return True # 아무 학생도 못 본 경우


N = int(stdin.readline())
arr = [list(stdin.readline().split()) for _ in range(N)]
res = False

teacher = 0 # 선생의 수
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teacher += 1

func(0)
print('YES' if res else 'NO')
