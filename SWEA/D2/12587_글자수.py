tc = int(input())

for t in range(1, tc +1):
    str1 = input()
    str2 = input()


    m_cnt = 0

    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1

        if cnt > m_cnt:
            m_cnt = cnt

    print('#{} {}'.format(t,m_cnt))