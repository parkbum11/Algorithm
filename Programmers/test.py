def solution(genres, plays):
    answer = []
    dic = {}
    dic_info = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            for index, j in enumerate(dic_info[genres[i]].values()):
                if plays[j] < plays[i]:
                    dic_info[genres[i]].values().insert(index, i)
                    break
                elif plays[j] == plays[i]:
                    if j > i:
                        dic_info[genres[i]].values().insert(index, i)
                        break
            else:
                dic_info[genres[i]].values().append(i)
        else:
            dic[genres[i]] = plays[i]
            dic_info[genres[i]] = list(i)

    print(dic_info)
    print(dic)

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])