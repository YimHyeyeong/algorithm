tc = int(input())

for t in range(1, tc+1):
    str = input()

    word = ''
    for i in str:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            word += i

    print('#{} {}'.format(t, word))
