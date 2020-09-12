def solution():
    s = input()
    if s == '*':
        return 'STOP'

    for i in range(len(s) - 1):
        pairs = set()
        for x in range(len(s)):
            try:
                pair = s[x] + s[x + i + 1]
                if pair in pairs:
                    print('{} is NOT surprising.'.format(s))
                    return
                pairs.add(pair)
            except:
                break

    print('{} is surprising.'.format(s))
while 1:
    result = solution()
    if result == 'STOP':
        break

