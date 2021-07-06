def solution(table, languages, preference):
    result = []
    check_num = 0
    # 0 = SI, 1 = CONTENTS, 2 = HARDWARE, 3 = PORTAL, 4 = GAME
    for i in table:
        new_st = i.split()
        num = 0
        for index, j in enumerate(languages):
            if j in new_st:
                num += (6 - new_st.index(j)) * (preference[index])
        if num >= check_num:
            print(new_st[0])
            result.append(new_st[0])
            check_num = num
    if len(result) > 1: result.sort()
    answer = result[0]

    return answer

print(solution(
    ["SI JAVA JAVASCRIPT SQL PYTHON C#",
     "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
     "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
     "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
     "GAME C++ C# JAVASCRIPT C JAVA"],
    ["PYTHON", "C++", "SQL"],
    [7, 5, 5]
))