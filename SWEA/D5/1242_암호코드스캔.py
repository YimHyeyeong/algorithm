
pwd = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}   # 0 1 0 1 중 첫번째 0은 탐색을 하면서 암호인지 그냥 0인지 판단하기 어려움 그래서 그냥 뺌,
 # 첫번째 0을 빼고도 충분히 암호가 구별가능함, 키 값은 비율이고, 아래의 c2,c3,c4를 최종적으로 구한 값임 

# 암호코드의 첫번째 줄의 시작위치 또는 끝위치
def check_code():
    ans = 0
    # 행우선으로 순회(뒤에서 부터)
    for i in range(N): # i = 행
        j = M * 4 - 1  # 밑에서 값을 10진수 -> 2진수 로 바꾸면서 가로의 길이가 4배 늘어남
        while j >= 0:
            # 암호코드의 첫줄의 마지막 위치를 판단, 뒤에서 부터 탐색함, 
            if arr[i][j] == 1 and arr[i - 1][j] == 0: #위치의 값이 1이고, 그 위치의 바로 위의 값이 0이면 암호배열의 제일 윗줄이라고 판단.
                # 8개의 패턴을 처리한다.
                read = []
                for _ in range(8):
                    c2 = c3 = c4 = 0
                    while arr[i][j] == 0: j -= 1   
                    while arr[i][j] == 1: c4 += 1; j -= 1 # 0 1 0 1 에서 제일 마지막의 1의 개수를 c4에 저장
                    while arr[i][j] == 0: c3 += 1; j -= 1
                    while arr[i][j] == 1: c2 += 1; j -= 1
                    # 최소 개수를 찾아서 key값 계산
                    min_cnt = min(c2, c3, c4)   # 암호가 문제에 나와있는 비율로 나오지만은 않음, 2배로 늘 수 있고 3배가 될 수 있음. 
                    read.append(pwd[(c2//min_cnt, c3//min_cnt, c4//min_cnt)]) # 제일 작은 값은 무조건 = 1, 개수 중 제일 적은 것을 개수들에 각각 나누면 암호의 원래 비율이 나옴 

                even = read[0] + read[2] + read[4] + read[6]
                odd = read[1] + read[3] + read[5] + read[7]
                if (odd * 3 + even) % 10 == 0:  # 10의 배수인지 판단
                    ans += odd + even
            j -=1  # 1을 만나지 못했을 경우 계속 오른쪽에서 왼쪽으로 탐색하기 위해 j를 -1
    return ans

# 16진수 문자열 ==> 2진수 정수 리스트 [0, 0, 0, 1, 1, 0, ...]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
    # 2진수 형태로 저장
    for i in range(N):
        tmp = input() # 배열을 한 줄씩 받아서
        for j in range(M):
            n = int(tmp[j], 16) # 10진수로 변환
            arr[i].append(1 if n & 8 else 0)  # n & 8 == n & (1<<3) 
            arr[i].append(1 if n & 4 else 0)  # 모든 숫자를 2진수로 바꿔서 리스트에 저장
            arr[i].append(1 if n & 2 else 0)
            arr[i].append(1 if n & 1 else 0)

    print('#{} {}'.format(tc, check_code()))