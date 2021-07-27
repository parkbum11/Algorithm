from itertools import combinations

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = sorted(orders[i])
    for i in course:
        dic = {}
        maxx = 0
        for order in orders:
            li = list(combinations(order, i))
            for j in li:
                st = ''.join(j)
                if st in dic: dic[st] += 1
                else: dic[st] = 1
                if dic[st] > maxx:maxx = dic[st]
        if maxx <= 1: continue
        for key, value in dic.items():
            if value == maxx: answer.append(key)
    print(sorted(answer))
    return sorted(answer)

# 다른사람 풀이
# import collections
# import itertools
#
# def solution2(orders, course):
#     result = []
#
#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)
#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
#         print(result)
#     return [''.join(v) for v in sorted(result)]

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
# solution2(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])