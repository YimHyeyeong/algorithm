T = int(input())

number_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, 1 + T):

    n = list(map(str, input().split()))

    number_list = list(map(str, input().split()))

    res = [0] * 10

    for q in number_list:
        res[number_alpha.index(q)] += 1

    print(n[0])
    for w in range(10):
        print('{} '.format(number_alpha[w]) * res[w])