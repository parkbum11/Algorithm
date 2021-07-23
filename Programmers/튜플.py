def solution(s):
    answer = []
    new_s = s[1:-1].split('},{')
    new_s[0] = new_s[0][1:]
    new_s[-1] = new_s[-1][:-1]
    for i in range(len(new_s)):
        sss = new_s[i].split(',')
        new_s[i] = sss
    for i in range(len(new_s)):
        new_s[i] = (len(new_s[i]), new_s[i])
    new_s.sort()
    print(new_s)
    for num, i in new_s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
                break
    print(answer)
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# solution("{{123}}")
# solution("{{20,111},{111}}")