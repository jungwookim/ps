input = __import__('sys').stdin.readline

def solution():
    n, k = map(int, input().split())
    shared_cards = list(map(int, input().split()))
    team_cards = list(map(int, input().split()))

    comb_all = []

    for sc in shared_cards:
        for tc in team_cards:
            comb_all.append([sc * tc, sc, tc])

    sorted_comb_all = sorted(comb_all, key = lambda x : -x[0])

    use_card = set()
    for comb in sorted_comb_all:
        if comb[2] in use_card:
            pass
        else:
            use_card.add(comb[2])
            ans = comb[0]
            k -= 1
            if k == -1:
                break
    print(ans)

solution()