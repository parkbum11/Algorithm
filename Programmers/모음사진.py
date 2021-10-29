def solution(word):
    wordN = {'A':0,'E':1,'I':2,'O':3,'U':4}
    word = list(word)
    org = 5**5
    answer = 0
    for i in word:
        answer += wordN[i]*(org-1)//4
        org //= 5
    answer += len(word)
    return answer