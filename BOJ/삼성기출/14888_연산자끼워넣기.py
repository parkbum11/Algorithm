import sys
sys.stdin = open('input.txt', 'r')

def DFS(num, lo):
    global maxx, minn
    if lo == N:
        if num > maxx: maxx = num
        if num < minn: minn = num
        return

    for i in range(4):
        if info[i] == 0: continue
        if i == 0:
            info[i] -= 1
            DFS(num + A[lo], lo + 1)
            info[i] += 1
        if i == 1:
            info[i] -= 1
            DFS(num - A[lo], lo + 1)
            info[i] += 1
        if i == 2:
            info[i] -= 1
            DFS(num * A[lo], lo + 1)
            info[i] += 1
        if i == 3:
            info[i] -= 1
            if num < 0: DFS((abs(num) // A[lo]) * (-1), lo + 1)
            else: DFS(num // A[lo], lo + 1)
            info[i] += 1

N = int(input())
A = list(map(int, input().split()))
# + - * /
info = list(map(int, input().split()))
maxx, minn = float('-inf'), float('inf')
DFS(A[0], 1)
print(maxx)
print(minn)