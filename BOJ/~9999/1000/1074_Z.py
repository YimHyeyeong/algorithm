# 분할정복

from sys import stdin

N, r,c = map(int,stdin.readline().split())

res = 0


# 4개의 영역으로 계속 분할해가기
while N != 0:
    N -= 1 # N에 1을 먼저 빼기 때문에
    
    # 1사분면
    if r < 2 ** N and c < 2 ** N:  # N의 제곱을 기준으로 몇사분면인지 확인
        res += (2**N) * (2**N) * 0 # 각 사분면의 시작 값임 1사분면의 시작값은 0
    # 2사분면
    elif r < 2**N and c >= 2** N:
        res += (2**N) * (2**N) * 1
        c -= 2**N # 가로가 2 ** N 만큼 줄어드니까
    # 3사분면
    elif r >= 2**N and c < 2 ** N:
        res += (2**N) * (2**N) * 2
        r -= 2 ** N
    # 4사분면
    else:
        res += (2**N) * (2**N) * 3
        r -= 2 ** N
        c -= 2**N

print(res)


# 재귀
N, r, c = map(int, input().split())

def sol(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))
    # sol( N-1, int(r/2), int(c/2) ) 는 이제 4의 배수하기 이전의 값
    # 2*(r%2)+(c%2)은 가장 작은 사각형 안에서의 위치
print(sol(N, r, c))
