


def finds(s_idx, W_len):
    if (s_idx + W_len - 1) >= len(sen):
        return 0
    for i in range(W_len):
        if sen[s_idx + i] != st[i]:
            return 0

    return 1



tc = 10
for t in range(1, tc +1):
    n = int(input())
    st = input()
    sen = input()

    cnt = 0
    for i in range(len(sen)):
        res = finds(i, len(st))
        if res == 1:
            cnt += 1


    print('#{} {}'.format(t, cnt))
