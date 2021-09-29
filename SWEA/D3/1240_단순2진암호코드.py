import sys
sys.stdin = open("text.txt","r")


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