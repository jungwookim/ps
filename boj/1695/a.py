from collections import deque
input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(str, input().split()))

    cnt_list = []
    for i in range(n):
        cnt = 0
        left = deque(a[0:i]) # 오른쪽 부터 뺌
        right = deque(a[i+1:]) # 왼쪽부터 뺌

        # deque로 넣었따 뺐다 해야할 듯
        while len(left) != 0:
            if len(right) == 0:
                print('cnt 1++', left)
                cnt += len(left)
                break
            if left[-1] == right[0]:
                left.pop()
                right.popleft()
            else:
                if right[0] in left:
                    right.appendleft(left[-1])
                elif left[-1] in right:
                    
                print('cnt 2++')
                left.append(right[0])
                cnt += 1
        print('add cnt', cnt)
        cnt_list.append(cnt)

    print(min(cnt_list))

solution()