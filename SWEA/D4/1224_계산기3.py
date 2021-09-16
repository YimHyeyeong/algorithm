for tc in range(1,11):
    N = int(input())
    Data = input()
    stack = []
    num_lst = []

    icp = {'*':2, '+':1, '(':3} 
    isp = {'*':2, '+':1, '(':0} 

    for i in range(N):
        if Data[i].isdigit():
            num_lst.append(Data[i])

        else:
            if not stack:
                stack.append(Data[i])
                continue
            elif stack:
                if Data[i] == ')':
                   while stack[-1] != '(':
                       num_lst.append(stack.pop())
                   stack.pop()

                elif icp[Data[i]] > isp[stack[-1]]:
                    stack.append(Data[i])

                else:
                    while icp[Data[i]] <= isp[stack[-1]]:
                        num_lst.append(stack.pop())
                    stack.append(Data[i])

    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            stack.append(num_lst[i])

        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if num_lst[i] == "+":
                result = num1 + num2
            elif num_lst[i] == "*":
                result = num1 * num2

            stack.append(str(result))

    print(f'#{tc} {stack[0]}')