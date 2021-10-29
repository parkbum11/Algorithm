import sys
sys.stdin = open('input.txt', 'r')

def destoy(s, e):
    for i in range(s, e):
        marble[i] = 0

def Explosion(end):
    global marble
    result = [0, 0, 0, 0]
    a = []
    st, cnt, num = 0, 0, 0
    for i in range(1, end):
        if marble[i] == 0: continue
        if st == 0:
            st = i
            cnt = 1
            num = marble[i]
        else:
            if num == marble[i]:
                cnt += 1
            else:
                a.append([st, i, num, cnt])
                cnt = 1
                st = i
                num = marble[i]
    a.append([st, end, num, cnt])
    stack = []
    for i in a:
        print(stack)
        if len(stack) == 0: stack.append(i)
        else:
            if i[3] >= 4:
                result[i[2]] += i[3]
                destoy(i[0], i[1])
            elif stack[-1][2] == i[2]:
                if stack[-1][3] + i[3] >= 4:
                    b = stack.pop(-1)
                    result[i[2]] += i[3] + b[3]
                    destoy(b[0], i[1])
                else:
                    stack[-1][1] = i[1]
                    stack[-1][3] += i[3]
            elif stack[-1][2] != i[2]:
                stack.append(i)
    new_marble = [-1]

    for i in stack:
        new_marble.append(i[3])
        new_marble.append(i[2])
    if len(new_marble) >= N ** 2:
        marble = new_marble[:N ** 2]
    else:
        new_marble += [0] * ((N ** 2) - len(new_marble))
        marble = new_marble
    return result

def Attack(d, s):
    r, c = N // 2, N // 2
    attack_dir = {3: 0, 2: 1, 4: 2, 1: 3}
    dir = attack_dir[d]
    for _ in range(s):
        r, c = r + dr[dir], c + dc[dir]
        if not (0 <= r < N) or not (0 <= c < N): break
        who = info[r][c]
        marble[who] = 0

def MakeInfo():
    global info, marble, end
    r, c, num, dir, cnt_info = N // 2, N // 2, 1, 0, [1, 0]
    while True:
        for _ in range(cnt_info[0]):
            r, c = r + dr[dir], c + dc[dir]
            if r < 0 or c < 0 or r >= N or c >= N: return
            if arr[r][c] == 0 and end == N ** 2: end = num
            info[r][c] = num
            marble.append(arr[r][c])
            num += 1
        dir = (dir + 1) % 4
        cnt_info[1] += 1
        if cnt_info[1] == 2:
            cnt_info[0] += 1
            cnt_info[1] = 0

# main
answer = 0
dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0] # 좌 하 우 상 3, 2, 4, 1
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
info = [[0] * N for _ in range(N)]
marble = [-1]
end = N ** 2
MakeInfo()
for _ in range(M):
    d, s = map(int, input().split())
    Attack(d, s)
    for i in info: print(i)
    result = Explosion(end)
    for i in range(1, 4):
        answer += result[i] * i
print(answer)

