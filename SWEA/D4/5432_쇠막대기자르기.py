tc = int(input())

for t in range(1, tc+1):

    str = input()
    n = len(str)

    i = 0
    stick = 0
    cnt = 0
    while i < n :
        if i + 1 < n and str[i] == '(' and str[i+1] == ')':
            cnt += stick
            i += 2

        elif str[i] == '(':
            stick += 1
            i += 1

        elif str[i] ==')':
            stick -= 1
            cnt += 1
            i += 1

    print('#{} {}'.format(t, cnt))