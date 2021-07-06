import sys
sys.stdin = open("input.txt", "r")

from itertools import combinations

a = input()
b = input()
li = []
result = 1
for i in range(1, len(a) + 1):
    li.append(list(combinations(a, i)))
for i in range(len(b), 0, -1):
    arr = list(combinations(b, i))
    for a in arr:
        for l in li:
            if a in l:
                result = len(a)
                break
        if result != 1: break
    if result != 1: break
print(result)