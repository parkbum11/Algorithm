# def solution(numbers):
#     answer = []
#     for number in numbers:
#         b = bin(number)[2:]
#         while True:
#             new_b = b
#             number += 1
#             bb = bin(number)[2:]
#             max_len = max(len(b), len(bb))
#             if len(b) < max_len:
#                 new_b = ('0' * (max_len - len(b))) + new_b
#             elif len(bb) < max_len:
#                 bb = ('0' * (max_len - len(bb))) + bb
#             cnt = 0
#             for i in range(max_len):
#                 if new_b[i] != bb[i]: cnt += 1
#                 if cnt > 2: break
#             else:
#                 answer.append(number)
#                 break
#     return answer

def solution(numbers):
    answer = []
    for number in numbers:
        b = bin(number)[2:][::-1]
        cnt = 0
        for i, v in enumerate(b):
            if v == '0':
                cnt = i - 1
                break
        else: cnt = len(b) - 1
        if cnt < 0: cnt = 0
        answer.append(number + (2 ** cnt))
    print(answer)
    return answer

solution([10])