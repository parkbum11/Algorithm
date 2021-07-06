def solution(genres, plays):
    answer = []
    dic = {}
    dic_info = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            for index, j in enumerate(dic_info[genres[i]]):
                if plays[j] < plays[i]:
                    dic_info[genres[i]].insert(index, i)
                    break
                elif plays[j] == plays[i]:
                    if j > i:
                        dic_info[genres[i]].insert(index, i)
                        break
            else:
                dic_info[genres[i]].append(i)
        else:
            dic[genres[i]] = plays[i]
            dic_info[genres[i]] = [i]

    dic_sorted = sorted(dic.items(), reverse=True, key=lambda item: item[1])
    for i in dic_sorted:

        if len(dic_info[i[0]]) <= 1:
            answer.append(dic_info[i[0]][0])
        else:
            answer.append(dic_info[i[0]][0])
            answer.append(dic_info[i[0]][1])

    return answer