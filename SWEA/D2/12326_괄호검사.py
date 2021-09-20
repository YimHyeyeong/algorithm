tc = int(input())

for t in range(1, tc +1):

    s = input()
    check = 0  # 괄호검사 실패할 경우 1, 성공할 경우 0
    stack = []
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '(' or s[i] == '{':
            stack.append(s[i])

        if s[i] == ')':
            if not stack:  # 스택이 비었다면 1 
                check = 1

            else:
                if stack[-1] != '(': # 짝이 맞지 않을 경우 1
                    check = 1
                stack.pop()  # 짝이 맞다면 pop

        if s[i] == '}':
            if not stack:
                check = 1

            else:
                if stack[-1] != '{':
                    check = 1
                stack.pop()

        if check == 1 :
            break
        i += 1

    if stack:
        check = 1

    if check == 0:
        print('#{} 1'.format(t))
    else :
        print('#{} 0'.format(t))
