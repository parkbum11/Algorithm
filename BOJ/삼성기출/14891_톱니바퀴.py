import sys
sys.stdin = open('input.txt', 'r')

# no batter than me
def DFS(a, dir):
    flag[a] = 1
    if a + 1 < 4 and flag[a + 1] == 0:
        x, y = arr[a][(info[a] + 2) % 8], arr[a + 1][((info[a + 1] - 2) + 8) % 8]
        if x != y: DFS(a + 1, -dir)
    if a - 1 >= 0 and flag[a - 1] == 0:
        x, y = arr[a][((info[a] - 2) + 8) % 8], arr[a - 1][(info[a - 1] + 2) % 8]
        if x != y: DFS(a - 1, -dir)
    info[a] = (info[a] - dir + 8) % 8

arr = [input() for _ in range(4)]
info, result = [0, 0, 0, 0], 0
K = int(input())
for i in range(K):
    a, dir = map(int, input().split())
    a -= 1
    flag = [0, 0, 0, 0]
    DFS(a, dir)
for i in range(4):
    if arr[i][info[i]] == '1': result += 2**i
print(result)
