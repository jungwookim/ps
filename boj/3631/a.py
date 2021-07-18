input = __import__('sys').stdin.readline

def is_invalid(s):
    if s[0].isupper():
        return True
    if s[0] == '_':
        return True
    if s[-1] == '_':
        return True
    meet_upper_case = False
    meet_underscore_case = False
    for i, char in enumerate(s):
        if char.isupper():
            meet_upper_case = True
        if char == '_':
            if s[i + 1] == '_':
                return True
            meet_underscore_case = True

    return meet_underscore_case and meet_upper_case
   
def is_cpp(s):
    return s[0] != '_' and s[-1] != '_' and '_' in s

def is_java(s):
    if not s[0].islower():
        return False
    for char in s:
        if char.isupper():
            return True
    return False

def java_to_cpp(s):
    new_s = []
    for char in s:
        if char.isupper():
            new_s.append('_')
            new_s.append(char.lower())
        else:
            new_s.append(char)
    return ''.join(new_s)

def cpp_to_java(s):
    new_s = []
    sign = False
    for char in s:
        if char == '_':
            sign = True
            continue
        else:
            if sign:
                new_s.append(char.upper())
                sign = False
            else:
                new_s.append(char)
    return ''.join(new_s)

def solution():
    a = input().strip()

    if is_invalid(a):
        print('Error!')
        return

    if is_java(a):
        print(java_to_cpp(a))
        return

    if is_cpp(a):
        print(cpp_to_java(a))
        return
    print(a)
solution()
