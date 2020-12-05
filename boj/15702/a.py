input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    problems = list(map(int, input().split()))
    scores = dict()

    for _ in range(m):
        number, *result = input().split()
        for i, ri in enumerate(result):
            key = int(number)
            if ri == 'O':
                if key in scores:
                    scores[key] += problems[i]
                else:
                    scores[key] = problems[i]
            else:
                if key not in scores:
                    scores[key] = 0

    max_score = max(scores.values())

    i_candis = []

    for i, score in scores.items():
        if score == max_score:
            i_candis.append(i)

    print(min(i_candis), max_score)

solution()
