def extract_number(filename):
    return int("".join(filter(lambda s: s.isdigit(), filename)))
    
def solution(arr):
    sorted_arr = sorted(arr, key=extract_number)
    return sorted_arr

print(solution(["file01", "file10", "file2"]))
