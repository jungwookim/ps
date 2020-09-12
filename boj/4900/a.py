def mapper(n):
    n = int(n)
    if n == 0:
        return '0111111', '063'
    if n == 1:
        return '0001010', '010'
    if n == 2:
        return '1011101', '093'
    if n == 3:
        return '1001111', '079'
    if n == 4:
        return '1101010', '106'
    if n == 5:
        return '1100111', '103'
    if n == 6:
        return '1110111', '119'
    if n == 7:
        return '0001011', '011'
    if n == 8:
        return '1111111', '127'
    if n == 9:
        return '1101011', '107'

code_dic = {}
for i in range(10):
    code_dic[i] = mapper(i)[1]

code_rev_dic = { v: str(k) for k, v in code_dic.items() }


def solution():
    s = input()
    if s == 'BYE':
        return 'STOP'

    a, temp_b = s.split('+')
    b, _ = temp_b.split('=')

    n_a = len(a) // 3
    n_b = len(b) // 3

    a_dp = ''
    b_dp = ''
    for i in range(n_a):
        a_dp += code_rev_dic[a[i * 3 : (i + 1) * 3]]
    for i in range(n_b):
        b_dp += code_rev_dic[b[i * 3 : (i + 1) * 3]]

    total = str(int(a_dp) + int(b_dp))
    ans = ''
    for char in total:
        ans += mapper(char)[1]

    print(s+ans)

while 1:
    message = solution()
    if message == 'STOP':
        break
