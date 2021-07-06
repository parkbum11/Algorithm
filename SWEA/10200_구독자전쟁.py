import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1 + int(input())):
    N, A, B = map(int, input().split())
    maxx, minn = min(A, B), 0
    if (A + B) - N > 0:
        minn = (A + B) - N
    print('#{} {} {}'.format(t, maxx, minn))