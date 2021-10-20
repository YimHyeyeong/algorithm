tc = int(input())

for t in range(1, tc +1):

    s = input()
    check = 0
    stack = []
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '(' or s[i] == '{':
            stack.append(s[i])

        if s[i] == ')':
            if not stack:
                check = 1

            else:
                if stack[-1] != '(':
                    check = 1
                stack.pop()

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
