from collections import defaultdict

# dfs or stack <-> backtracking
def solution(tickets):
    it = defaultdict(list)
    for dpt, des in sorted(tickets):
        it[dpt].append(des)

    result = []
    def dfs(loc):
        while it[loc]:
            dfs(it[loc].pop(0))
        result.append(loc)

    dfs("JFK")

    return result[::-1]

print(solution([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(solution([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(solution([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
