def solution(array):
    answer = []
    info = [-1, 1]
    maxx = max(array)
    for i, v in enumerate(array):
        if v == maxx:
            answer.append(-1)
        else:
            cnt = 1
            an = -1
            while True:
                if an != -1:
                    answer.append(an)
                    break
                for j in info:
                    new_index = i + (j * cnt)
                    if new_index < 0 or new_index >= len(array):
                        continue
                    if array[new_index] > v:
                        an = new_index
                        break
                cnt += 1
    return answer