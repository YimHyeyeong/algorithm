tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    print('#{}'.format(t))
    stack = []
    for i in range(n):

        A = input().split()

        if A[0] == 'i':
            stack.append(int(A[1]))

        elif A[0] == 'o':
            if stack:
                print(stack.pop())
            else:
                print("empty")
                
        elif A[0] == "c":
            print(len(stack))