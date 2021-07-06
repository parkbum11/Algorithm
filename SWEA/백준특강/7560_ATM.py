import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1 + int(input())):
    N = int(input())
    p = list(map(int, input().split()))
    p.sort()
    result, summ = 0, 0
    for pp in p:
        result = (result + pp)
        summ += result
    print('#{} {}'.format(t, summ))
