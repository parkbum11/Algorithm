def solution(ads):
    answer = 0
    ads.sort()
    sec = ads[0][0]
    while ads:
        index, value = -1, 0
        for i, v in enumerate(ads):
            if v[0] <= sec:
                if value < (sec + 5 - v[0]) * v[1]:
                    index = i
                    value = (sec - v[0]) * v[1]
            else:
                break
        ads.pop(index)
        answer += value
        sec += 5
    return answer

solution([[0, 1], [0, 2], [6, 3], [8, 4]])