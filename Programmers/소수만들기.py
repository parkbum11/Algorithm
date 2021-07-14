from itertools import combinations

def solution(nums):

    answer = 0

    for i in list(combinations(nums, 3)):
        summ = sum(i)
        for j in range(2, summ):
            if summ % j == 0:
                break
        else:
            answer += 1
    return answer

solution([1,2,7,6,4])