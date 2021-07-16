def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        cnt = 1
        for j in range(1, i // 2 + 1):
            if i % j == 0: cnt += 1
        if cnt & 1: answer -= i
        else: answer += i

    return answer

# 다른사람풀이
# 제곱근은 약수가 홀수 나머지는 짝수
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer