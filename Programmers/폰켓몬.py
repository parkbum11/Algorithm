def solution(nums):
    answer = 0
    length_nums = len(nums) // 2
    nums = len(set(nums))
    if nums > length_nums: answer += length_nums
    else: answer += nums
    return answer

solution([3,3,3,2,2,4])