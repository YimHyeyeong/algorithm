from sys import stdin


while True:
    a, b = map(int, stdin.readline().split())
    if (a,b) == (0,0):
        break

    if b // a > 0 and (b%a) == 0:
        print('factor')
    elif a // b > 0 and (a%b) == 0:
        print('multiple')
    else:
        print('neither')

