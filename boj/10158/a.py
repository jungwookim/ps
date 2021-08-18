input = __import__('sys').stdin.readline

def solution():
    w, h = map(int, input().split())
    x, y = map(int, input().split())
    t = int(input())

    x_move_cnt = (x+t) % (2*w)
    y_move_cnt = (y+t) % (2*h)
    pos_x = x_move_cnt if w > x_move_cnt else 2 * w - x_move_cnt
    pos_y = y_move_cnt if h > y_move_cnt else 2 * h - y_move_cnt
    print(pos_x, pos_y)
solution()