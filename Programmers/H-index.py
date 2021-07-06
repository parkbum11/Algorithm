def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i >= citations[i]:
            answer = i
            break
    return answer