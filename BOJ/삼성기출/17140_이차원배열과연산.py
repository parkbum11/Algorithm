import sys
sys.stdin = open("input.txt", "r")


def rSort():
    global maxc
    r_len = 0
    for i in range(maxr):
        dict, li = {}, []
        for j in range(maxc):
            if arr[i][j] == 0:
                break
            if arr[i][j] in dict:
                dict[arr[i][j]] += 1
            else:
                dict[arr[i][j]] = 1

        for key, value in dict.items():
            li.append((key, value))

        li.sort(key=lambda x : (x[1], x[0]))
        num = len(li) * 2
        if num > r_len: r_len = num

        for index, (a, b) in enumerate(li[:100]):
            arr[i][index * 2] = a
            arr[i][index * 2 + 1] = b

    if r_len > maxc: maxc = r_len

def cSort():
    global maxr
    c_len = 0
    for j in range(maxc):
        dict, li = {}, []
        for i in range(maxr):
            if arr[i][j] == 0:
                break
            if arr[i][j] in dict:
                dict[arr[i][j]] += 1
            else:
                dict[arr[i][j]] = 1

        for key, value in dict.items():
            li.append((key, value))

        li.sort(key=lambda x: (x[1], x[0]))
        num = len(li) * 2
        if num > c_len: c_len = num

        for index, (a, b) in enumerate(li[:100]):
            arr[index * 2][j] = a
            arr[index * 2 + 1][j] = b

    if c_len > maxr: maxr = c_len

# main
r, c, k = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
answer = 0
maxr, maxc = 3, 3

for i in range(3):
    li = list(map(int, input().split()))
    for j in range(3): arr[i][j] = li[j]

while arr[r - 1][c - 1] != k:
    if answer > 100:
        answer = -1
        break
    if maxr >= maxc:
        rSort()
    else:
        cSort()
    answer += 1

print(answer)