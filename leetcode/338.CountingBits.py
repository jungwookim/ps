from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        max_num = 100005
        d = [0] * max_num
        d[0] = 0
        d[1] = 1
        d[2] = 1
        d[3] = 2
        for i in range(max_num):
            if i < 4:
                continue
            for j in range(2, 18):
                if 2**j <= i < min(2**(j+1), max_num):
                    d[i] = d[i - 2**j] + 1
        return d[:n+1]

def countBits(n):
    # 결과 배열을 0으로 초기화
    ans = [0] * (n + 1)
    
    # 1부터 n까지 반복
    for i in range(1, n + 1):
        # 동적 프로그래밍 관계식을 사용하여 1의 개수 계산
        ans[i] = ans[i >> 1] + (i & 1)
    
    return ans

# 예시 사용:
print(countBits(2))  # 출력: [0, 1, 1]
print(countBits(5))  # 출력: [0, 1, 1, 2, 1, 2]
