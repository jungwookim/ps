input = __import__('sys').stdin.readline

def solution():
    a ={"pi", "ka", "chu", ""}
    s = input().strip()

    l = 0
    r = 0

    while r < len(s):
        word = s[l:r+1]
        if word in a:
            r += 1
            l = r
        else:
            r += 1
    if s[l:r+1] in a:
        print("YES")
    else:
        print("NO")

solution()
