input = __import__('sys').stdin.readline
import math
def solution():
    hp1, atk1, hp2, atk2 = map(int, input().split())
    p, s = map(int, input().split())

    # 용사가 죽는 시점
    min_step1 = math.ceil(hp1 / atk2)

    # 마왕이 체력 p 이하로 떨어지는 시점
    min_step2 = math.ceil((hp2 - p) / atk1)

    # 마왕의 체력이 p 이하로 먼저 떨어질 때
    if min_step1 > min_step2:
        if hp2 - atk1 * min_step2 >= 1:
            hp2 = hp2 - atk1 * min_step2 + s
            delta = min_step1 - min_step2
            if hp2 - atk1 * delta <= 0:
                print('Victory!')
            else:
                print('gg')
        else:
            print('Victory!')
    elif min_step1 < min_step2: # 용사가 먼저 죽을 때
        print('gg')
    else: # 같은 턴에 용사가 죽더라도 마왕이 먼저 죽을 수 있음
        if hp2 - atk1 * min_step1 <= 0:
            print('Victory!')
        else: # 마왕은 회복하면서 
            print('gg')



solution()
