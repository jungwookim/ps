import string
input = __import__('sys').stdin.readline

def calc_alphabet_count(s: str):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for si in s:
        d[si] += 1

    return d
        
def solution():
    encrypted_s = input().strip()
    s = input().strip()
    target_d = calc_alphabet_count(s)

    current_d = None
    for i in range(len(encrypted_s)):
        if current_d is None:
            current_d = calc_alphabet_count(encrypted_s[i:i+len(s)])
        if target_d == current_d:
            return "YES"
        
        current_d[encrypted_s[i]] -= 1
        if i + len(s) < len(encrypted_s):
            current_d[encrypted_s[i+len(s)]] += 1
    else:
        return "NO"



for _ in range(int(input())):
    print(solution())