def solution(arr):
    for num in arr:
        if max(arr) <= 0:
            return 1
    l = [x for x in range(min(arr), max(arr) + 1)]
    res = set(l) - set(arr)
    if not res:
        return max(arr) + 1
    else:
        return res

print(solution([-1, -3]))