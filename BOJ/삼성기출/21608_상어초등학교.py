import sys
sys.stdin = open('input.txt', 'r')

dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
N = int(input())
arr = [[0] * N for _ in range(N)]
all_students = [0] * (N**2 + 1)
for _ in range(N ** 2):
    students = list(map(int, input().split()))
    all_students[students[0]] = students[1:]
    new_arr = []
    max_friend = 0
    max_none = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt_friend = 0
                cnt_none = 0
                for k in range(4):
                    r, c = i + dr[k], j + dc[k]
                    if r < 0 or r >= N or c < 0 or c >= N:
                        continue
                    if arr[r][c] in students:
                        cnt_friend += 1
                    elif arr[r][c] == 0:
                        cnt_none += 1
                if max_friend < cnt_friend:
                    max_friend = cnt_friend
                new_arr.append((i, j, cnt_friend, cnt_none))

    sits = []
    for ii in range(len(new_arr)):
        if new_arr[ii][2] == max_friend:
            if max_none < new_arr[ii][3]:
                max_none = new_arr[ii][3]
            sits.append((new_arr[ii][0], new_arr[ii][1], new_arr[ii][3]))

    for k in sits:
        if k[2] == max_none:
            arr[k[0]][k[1]] = students[0]
            break

result = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            r, c = i + dr[k], j + dc[k]
            if r < 0 or c < 0 or r >= N or c >= N:
                continue
            if arr[r][c] in all_students[arr[i][j]]:
                cnt += 1
        if cnt == 0:
            cnt += 1
        result += 10 ** (cnt - 1)
print(result)

# dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
# N = int(input())
# arr = [[0] * N for _ in range(N)]
# flag = [0] * (N**2 + 1)
# for i in range(N**2):
#     sits = {}
#     max_num = 0
#     students = list(map(int, input().split()))
#     if i == 0:
#         arr[1][1] = students[0]
#         flag[students[0]] = (1, 1)
#     else:
#         for j in students[1:]:
#             if flag[j] != 0:
#                 for k in range(4):
#                     rr, cc = flag[j][0] + dr[k], flag[j][1] + dc[k]
#                     if rr < 0 or rr >= N or cc < 0 or cc >= N or arr[rr][cc] != 0:
#                         continue
#                     if (rr, cc) in sits:
#                         sits[(rr, cc)] += 1
#                         if max_num < sits[(rr, cc)]:
#                             max_num = sits[(rr, cc)]
#                     else:
#                         sits[(rr, cc)] = 1
#
#     sits2 = {}
#     max_num = 0
#     for key, value in sits.items():
#         if value == max_num:
#             sits2[key] = 0
#     for value in sits.keys():
#         cnt = 0
#         for k in range(4):
#             rr, cc = value[0] + dr[k], value[1] + dc[k]
#             if arr[rr][cc] == 0:
#                 cnt += 1
#         sits2[key] = cnt
#         if max_num < cnt:
#             max_num = cnt
#
#     sits3 = []
#     for key, value in sits2.items():
#         if value == max_num:
#             sits3.append(key)
#     sits3.sort()
#     print(sits3)
#     arr[sits3[0][0]][sits3[0][1]] = 1
#     flag[students[0]] = sits3[0]
#
# print(arr)
