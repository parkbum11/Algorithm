import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    result = 'No'
    for i in range(1, 10):
        if (N // i) < 10 and (N % i) == 0:
            result = 'Yes'
            break
    print('#{} {}'.format(t, result))