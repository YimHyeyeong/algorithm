for tc in range(10):
    n = int(input())
 
    board = list(map(str,input()))
    cal = []
    num = []
 
    for q in board:
        if q == '+' or q == '*':
            cal.append(q)
 
        else:
            num.append(int(q))

    res = 0

    temp = 1
 
    for w in range(int(n/2)):
        if w != int(n/2)-1:

            if cal[w] == '+':
                if temp != 1:
                    temp *= num[w]
 
                    res += temp
                    temp = 1
 
                else:
                    res += num[w]
 
            else:
                temp *= num[w]
        else:
            if cal[w] == '+':
                if temp != 1:
                    temp *= num[w]
                    res += temp
                else:
                    res += num[w]
                res += num[w + 1]
            else:
                temp *= num[w] * num[w+1]
 
                res += temp
 
    print('#{} {}'.format(tc+1,res))