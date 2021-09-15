def check(lst):
    for i in range(len(lst)//2):
        if lst[i]!=lst[-i-1]:
            return False
    return True

for tc in range(1,11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))
    max_v = 1 


    for length in range(100,1,-1):
        if max_v >= length:
            break
        for idx in range(100-length+1):
            if max_v == length:
                break
            for lst, lst2 in zip(arr, arr2):
                if check(lst[idx:idx+length]) or check(lst2[idx:idx+length]):
                    max_v = length
                    break
    print('#{} {}'.format(tc,max_v))