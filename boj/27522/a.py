input = __import__('sys').stdin.readline

def solution():
    records = [input().strip() for _ in range(8)]
    records.sort(reverse=True)

    team_order = [e.split(" ")[1] for e in records]

    b_point = 0
    a_point = 0

    for i, team in enumerate(team_order):
        point = i + 1
        if i == 6:
            point += 1
        if i == 7:
            point += 2

        if team == 'B':
            b_point += point
        if team == 'R':
            a_point += point

    if b_point > a_point:
        print("Blue")
    else:
        print("Red")

solution()
    