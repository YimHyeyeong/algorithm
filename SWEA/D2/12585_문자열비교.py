T = int(input())

for i in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    res = 0
    for j in range(M-N+1):
        if str2[j:j+N] == str1:
            res = 1

    print('#{} {}'.format(i,res))