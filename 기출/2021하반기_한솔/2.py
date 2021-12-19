def solution(s):
    answer = 0
    length = len(s)
    cnt = 1
    li = set()
    while cnt < length + 1:
        for i in range(length):
            if i + cnt > length:
                break
            t = set(s[i:i + cnt])
            if len(t) == cnt:
                li.add(s[i:i + cnt])
        cnt += 1
    answer = len(li)
    print(answer)
    return answer

solution("abac")