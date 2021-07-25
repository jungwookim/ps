x, y = map(int, input().split())

cnt = 0

if x < y:
    x, y = y, x

cx, cy = 0, 0

i = 0 # x turn, 1 -> y turn
import math
while int(math.ceil(cx)) < x or int(math.ceil(cy)) < y:
    if i == 0:
        delta = x - cx
        cnt += delta
        print('i', i, 'delta', delta)
        cx += delta
        if cy - (0.1 * delta) <= 0:
            cy = 0
        else:
            cy -= (0.1 * delta)
            
        i += 1
    else:
        delta = y - cy
        cnt += delta
        print('i', i, 'delta', delta)
        cy += delta
        if cx - (0.1 * delta) <= 0:
            cx = 0
        else:
            cx -= (0.1 * delta)
        i -= 1
    print(int(math.ceil(cx)) < x and int(math.ceil(cy)) < y, 'x', x, 'current', math.ceil(cx), 'y', y, 'current y', math.ceil(cy))

print(cnt)