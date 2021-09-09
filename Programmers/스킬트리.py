def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        num = 0
        i += skill
        for j in skill:
            location = i.index(j)
            if location < num: break
            else: num = location
        else: answer += 1
    return answer

solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"])