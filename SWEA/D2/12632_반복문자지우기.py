tc = int(input())

for t in range(1, tc +1):

    str = input()

    stack = []

    for i in str:
        if stack and stack[-1] == i: 
            stack.pop()
        else:
            stack.append(i)

    print('#{} {}'.format(t, len(stack)))