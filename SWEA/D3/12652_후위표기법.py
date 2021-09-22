def is_valid(s1, s2):  # 연산자의 우선순위를 파악하는 함수
    eval = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    if eval[s1] <= eval[s2]:  # top에 위치한 것이 비교할 연산자보다 우선 순위가 높을 경우 pop
        return True

    else:
        return False

tc = int(input())

for t in range(1, tc+1):
    s = input().rstrip()
    i = 0
    stack = []
    n = len(s)
    print('#{}'.format(t), end= ' ')

    while i < n :
        if s[i].isdigit():  # 피연산자일 경우 그냥 출력
            print(s[i], end='')

        elif s[i] == '(':  # 여는 괄호는 스택 밖에서 우선 순위가 가장 높기때문에 그냥 추가
            stack.append(s[i])

        elif s[i] == ')':
            while stack[-1] != '(':   # 여는 괄호를 만날 때까지 pop하고 출력
                print(stack.pop(), end='')
            stack.pop()  # 여는 괄호를 만날 경우 그냥 pop

        else:
            while stack and is_valid(s[i], stack[-1]):  # 스택이 비었지 않고 스택 안의 연산자가 비교할 연산자보다 우선 순위가 높을 경우 pop
                print(stack.pop(), end='') # 우선 순위가 낮아질 때까지 pop한 후 출력
            stack.append(s[i])
        i += 1

    while stack :   # 스택에 남아있는 모든 연산자를 출력!!
        print(stack.pop(), end='')

    print()


