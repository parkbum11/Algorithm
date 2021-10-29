import sys
sys.stdin = open("input.txt", "r")

def DFS(n, total):
    global answer, people
    print(people, total)
    if n == 10:
        answer = max(answer, total)
        return
    for i in range(4):
        p = people[i]
        new_p = people[i]
        if p >= 32: continue
        if new_p == 5 or new_p == 10 or new_p == 15:
            maxx = info[new_p][1]
            plus = info[new_p][2]
            new_p = info[new_p][0] - 1
            new_p += li[n]
            if new_p > maxx:
                new_p += plus
        else:
            new_p += li[n]
            if p <= 20 and new_p > 20:
                new_p = 32
            elif p > 20 and new_p > 31:
                new_p = 32
            if 21 <= p <= 23 and new_p > 23:
                new_p += 5
            elif 24 <= p <= 25 and new_p > 25:
                new_p += 3
        if new_p in people:
            continue
        people[i] = new_p
        DFS(n + 1, total + arr[new_p])
        people[i] = p

answer = 0
arr = [0] * 21
num = 2
for i in range(1, 21):
    arr[i] = num
    num += 2
arr += [13, 16, 19]
arr += [22, 24]
arr += [28, 27, 26]
arr += [25, 30, 35, 0]
info = [None] * 16
info[5] = [21, 23, 5]
info[10] = [24, 25, 3]
info[15] = [26, 28, 0]
li = list(map(int, input().split()))
people = [0, 0, 0, 0]
DFS(0, 0)
print(answer)