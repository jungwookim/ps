input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())

    card_by_column = [[] for _ in range(m)]

    for _  in range(n):
        sorted_cards = sorted(list(map(int, input().split())))
        for i, card in enumerate(sorted_cards):
            card_by_column[i].append(card)

    score = [0 for _ in range(n)]

    for col in card_by_column:
        maxv = max(col)
        for i, card in enumerate(col):
            if card == maxv:
                score[i] += 1
    
    max_score = max(score)

    for i, s in enumerate(score):
        if s == max_score:
            print(i+1, end=' ')

solution()
