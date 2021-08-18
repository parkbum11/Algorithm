def solution(arr):
    answer = []
    if len(arr) == 0:
        if arr[0][0] & 1: return [0, 1]
        else: return [1, 0]

    return answer