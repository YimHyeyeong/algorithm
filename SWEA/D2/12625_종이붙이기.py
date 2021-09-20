def func(n):
    if n == 10 :  # n이 10일 경우 나오는 경우의 수는 1개뿐
        return 1
    elif n == 20 :  # n이 20일 경우 나오는 경우의 수는 3
        return 3
    
    return func(n-10) + (2 * func(n-20))  
    # n은 n-1 했을 때 작은 네모를 하나 더 붙인 것일 뿐이고 경우의 수는 똑같음
    # n-2는 3가지의 방법이 가능하나 n-1에서 하나를 사용했기에 *2 


tc = int(input())

for t in range(1, tc+1):

    num = int(input())

    res = func(num)
    
    print('#{} {}'.format(t, res))