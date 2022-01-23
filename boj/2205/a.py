input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    power_set = []
    for i in range(1, 15):
        power_set.append(2**i)

    possible_set = set(range(1, n+1))
    def find_larger_closest_power_item(x, limit):
        candi = []
        for item in power_set:
            if item <= limit * 2:
                if item > x:
                    candi.append(item)

        return max(possible_set.intersection(set([c - x for c in candi])))

    a = range(1, n+1)
    reversed_a = reversed(a)
    reversed_ans = []
    for item in reversed_a:
        res = find_larger_closest_power_item(item, n)
        possible_set.remove(res)
        reversed_ans.append(res)


    for ans in list(reversed(reversed_ans)):
        print(ans)
    
solution()


# 이분 매칭, 유령 알고리즘