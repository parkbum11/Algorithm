import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

A, B = map(int, input().split())
result = 0
time = 0
q = deque()
q.append((A, B, 0))
while q:
    a, b, sec = q.popleft()
    if a < 0 or a > 200000 or b < 0 or b > 200000: continue
    if a == b:
        result = sec
        break
    sec += 1
    q.append((a + sec, b + 1, sec))
    q.append((a + sec, b - 1, sec))
    q.append((a + sec, b * 2, sec))
print(sec)
