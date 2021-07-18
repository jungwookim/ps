input = __import__('sys').stdin.readline

def solution():
    h, m, s = map(int, input().split())
    h_base = 30 * h
    m_base = 6 * m
    s_base = 6 * s

    m_add = 6 * s / 60
    h_add = (30 / 60) * (m + s / 60)
    a = [h_base + h_add, m_base + m_add, s_base]

    candi = []
    for i in range(3):
        for j in range(i+1, 3):
            x = abs(a[i] - a[j])
            y = 360 - x
            candi.append(x)
            candi.append(y)

    print(min(candi))
for _ in range(int(input())):
    solution()
