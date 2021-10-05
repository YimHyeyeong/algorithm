tc = int(input())

for t in range(1, tc+1):
    N = float(input())

    res = ''   # 2진수를 저장

    while N:
        N *= 2   # 10진수의 실수를 *2했을 때

        if N >= 1:   # 1보다 크다면 2진수의 자리가 1인 거 (N이 0보다 크고 1미만인 십진수이라서?)
            res += '1'
            N -= 1   # 다시 1을 빼고 곱해서 확인
        else:
            res += '0' # 1보다 작다면 0

        if len(res) > 12:
            res = 'overflow'
            break

    print('#{} {}'.format(t,res))

