tc = int(input())

for t in range(1, tc +1):

    st = input()

    k = ''
    for i in st:

        if i == 'b':
            k += 'd'

        elif i == 'd':
            k += 'b'

        elif i == 'p':
            k += 'q'

        else:
            k += 'p'

    print('#{}'.format(t), end= ' ')
    print(k[::-1])

