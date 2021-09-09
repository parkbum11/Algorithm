def solution(nodeinfo):
    answer = [[]]
    new_nodeinfo = []
    for i, info in enumerate(nodeinfo):
        info.append(i + 1)
        new_nodeinfo.append(info)
    new_nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    print(new_nodeinfo)


    # make tree

    return answer

# 다른 사람 풀이
# import sys
#
# sys.setrecursionlimit(10 ** 6)  # 이걸 안해주면 횟수제한에 걸려서 재귀가 막혀버림
#
# preorder = list()
# postorder = list()
#
#
# def solution(nodeinfo):
#     levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)  # 어떤 레벨이 있는지 파악
#     print(levels)
#     nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)),
#                    key=lambda x: (-x[1][1], x[1][0]))  # 노드좌표와 인덱스를 서로 연결 해 줌
#
#     order(nodes, levels, 0)
#
#     return [preorder, postorder]
#
#
# def order(nodeList, levels, curLevel):
#     print(preorder, postorder)
#     n = nodeList[:]
#     print(n)
#     cur = n.pop(0)
#     preorder.append(cur[0])
#     if n:
#         for i in range(len(n)):
#             if n[i][1][1] == levels[curLevel + 1]:
#                 if n[i][1][0] < cur[1][0]:
#                     order([x for x in nodeList if x[1][0] < cur[1][0]], levels, curLevel + 1)
#                 else:
#                     order([x for x in nodeList if x[1][0] > cur[1][0]], levels, curLevel + 1)
#     postorder.append(cur[0])


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])