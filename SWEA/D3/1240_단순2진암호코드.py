
# [1]
pwd = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}



# 암호코드의 첫번째 줄의 시작위치, 끝위치
# 무조건 앞에서부터 7개씩 끊으면 안 됨
# 거꾸로 가면서 1이 나오면 패턴 존재
def check():
    for i in range(N):
        for j in range(M-1, 0, -1):
            if arr[i][j] == '0' : continue
            # 암호코드의 마지막 위치 j에서 -55 하면 시작위치 나옴
            # 2번째 패턴 시작위치는 +7 아니면 뒤에서 부터 빼면서 가면 됨
            # 8개의 암호패턴을 읽어서 숫자로 변환
            read = []
            for s in range(j-55,j,7):
                read.append(pwd[arr[i][s: s+7]])  # 함수 get 써도 괜찮음

            odd = read[0] + read[2] + read[4] + read[6]
            even = read[1] + read[3] + read[5] + read[7]

            if (odd * 3 + even) % 10 == 0:
                return odd + even
            else:
                return 0

tc = int(input())

for t in range(1, tc + 1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    print('#{} {}'.format(t, check()))



########################################
# [2] 슬라이싱 안쓰고 푸는 방법

# 1,0의 개수를 세서 튜플로 처리
pwd = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}

# 암호코드의 첫번째 줄의 시작위치 또는 끝위치
def check_code():
    for i in range(N):
        for j in range(M - 1, 0, -1):
            if arr[i][j] == '0': continue
            # 암호코드의 마지막 열 위치 j, 시작 = j - 55

            read = []
            # 8개의 암호패턴을 읽어서 숫자로 변환
            idx = j
            for _ in range(8):
                # 0 1 0 1 의 개수를 카운팅한다.
                c1 = c2 = c3 = c4 = 0
                while arr[i][idx] == '1':   # 0 1 0 1 중 2번째 1들의 개수를 세서 저장
                    c4 += 1
                    idx -= 1
                while arr[i][idx] == '0':
                    c3 += 1
                    idx -= 1
                while arr[i][idx] == '1':
                    c2 += 1
                    idx -= 1  
                c1 = 7 - (c2 + c3 + c4)   # 첫번째 0을 제외한 나머지를 7에서 빼면 c1이 됨
                idx -= c1
                read.append(pwd[(c1, c2, c3, c4)])

            even = read[0] + read[2] + read[4] + read[6]
            odd = read[1] + read[3] + read[5] + read[7]

            if (odd * 3 + even) % 10 == 0:
                return odd + even
            else:
                return 0

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print('#{} {}'.format(tc, check_code()))



