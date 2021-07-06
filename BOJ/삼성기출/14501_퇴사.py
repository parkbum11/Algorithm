import sys
sys.stdin = open('input.txt', 'r')

def DFS(st, t, p, total):
    global result
    st += 1
    t -= 1
    if st == N:
        if t <= 0 and total > result: result = total
        elif total - p > result: result = total - p
        return
    if t == 0:
        for i in range(st, N):
            DFS(i, li[i][0], li[i][1], total + li[i][1])
    else:
        DFS(st, t, p, total)

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i, lili in enumerate(li):
    DFS(i, lili[0], lili[1], lili[1])
print(result)


# other1
n = int(input())
v = [0]*30
r = s = 0
while s < n:
    t, p = map(int, input().split())
    v[s+t] = max(v[s+t], r+p)
    s += 1
    r = max(r, v[s])
    print("r {}".format(r))
    print("s {}".format(s))
    print("t, p {} {}".format(t, p))
    print("vv {}".format(v))
    print('=========================================')
print(r)

# o2
n = int(input())
T, P = [0 for i in range(n + 1)], [0 for i in range(n + 1)]
for i in range(n):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

# dp[i]는 i번째날까지 일을 했을 때, 최대값이다.
dp = [0 for i in range(n + 1)]

for i in range(len(T) - 2, -1, -1):  # 역순으로 진행
    if T[i] + i <= n:  # 날짜를 초과하지 않을 경우.
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:  # 날짜를 초과할 경우.
        dp[i] = dp[i + 1]
print(dp[0])

# 03
n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

d = [0] * (n + 1)

for i in range(n):
    if i + t[i] <= n:
        d[i + t[i]] = max(d[i] + p[i], d[i + t[i]])
    d[i + 1] = max(d[i + 1], d[i])

print(d[n])
