
import sys
tc = int(sys.stdin.readline())

S = 1 << 21 # 집합

for t in range(tc):

    temp = sys.stdin.readline().split()

    if len(temp) == 2:
        cmd = temp[0]
        x = int(temp[1])

    else:
        cmd = temp[0]


    if cmd == 'add':
        S |= (1 << x)

    elif cmd == 'remove':
        S &= ~(1 << x) # S & 0

    elif cmd == 'check':
        if S & (1 << x):
            print(1)
        else:
            print(0)

        # 혹은 print((S & (1 << x )) >> x )

    elif cmd == 'toggle':
        S ^= (1 << x)

    elif cmd == 'all':
         S = (1 << 21) -1   # 10000 -> 1111

    elif cmd == 'empty':
        S = 1 << 21    # 100000000....


