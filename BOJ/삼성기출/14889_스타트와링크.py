import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations, permutations
N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]
li = []
for i in range(N):
    li.append(i)
cal = list(combinations(li, N // 2))
result = float('inf')
for i in range(len(cal) // 2):
    a = 0
    info = list(permutations(cal[i], 2))
    for x, y in info:
        a += power[x][y]
    info = list(permutations(cal[-(i + 1)], 2))
    for x, y in info:
        a -= power[x][y]
    if abs(a) < result:
        result = abs(a)
print(result)

#
N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

ret = []
def sol(start,link,s1,s2,i):
  if i == N:
    ret.append(abs(s1-s2))
    return
  if len(start) < N//2:
    start.append(i)
    temp = 0
    for j in start:
      temp += S[j][i] + S[i][j]
    sol(start,link,s1+temp,s2,i+1)
    start.pop()
  if len(link) < N//2:
    link.append(i)
    temp = 0
    for j in link:
      temp += S[j][i] + S[i][j]
    sol(start,link,s1,s2+temp,i+1)
    link.pop()
  return
sol([0],[],0,0,1)
print(min(ret))