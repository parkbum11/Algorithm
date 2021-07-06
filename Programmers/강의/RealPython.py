### map 활용
mylist = [[1, 2], [3, 4, 5], [6]]
# 원하는 출력 배열마다 길이를 하나의 리스트로
# 내 답
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer
# 파파답 답
def solution(mylist):
    return list(map(len, mylist))

###################################################################################################
### 목과 나머지 한번에
a, b = map(int, input().strip().split(' '))
d = [*divmod(a, b)]
print(d)
print(*divmod(a, b))

###################################################################################################
### 진법 관련

# 내 답
num, base = map(int, input().strip().split(' '))
a = int(str(num), base)
print(a)

# 파파답 답
num, base = map(int, input().strip().split(' '))
a = int(str(num), base)
print(a)


###################################################################################################
### 문자열 method

# 내 답
s = '가나다라'
n = 7
answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s

# 파파답 답
s, n = input().strip().split(' ')
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))

###################################################################################################
### 알파벳 출력하기

import string

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

###################################################################################################
#### 원본유지 정렬된 리스트

# my
list1 = [3, 2, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()

# good
list1 = [3, 2, 1]
list2 = sorted(list1)

###################################################################################################
### 2차원 리스트 뒤집기

# my
def solution(mylist):
    answer = []
    length = len(mylist)
    for i in range(length):
        a = []
        for j in range(length):
            a.append(mylist[j][i])
        answer.append(a)
    return answer

# good
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))

# zip
mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)
# (1, 40)
# (2, 50)
# (3, 60)

###################################################################################################
### i번째 원소와 i + 1 번재 원소

# my
def solution(mylist):
    answer = []
    for i in range(len(mylist) - 1):
        answer.append(abs(mylist[i] - mylist[i + 1]))
    return answer

# good (use zip)
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer


###################################################################################################
### 모든 멤버의 type 변환하기

# my
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(int(i))
    return answer

# good
list1 = ['1', '100', '33']
list2 = list(map(int, list1))


###################################################################################################
### map 함수 응용하기

# my
# input	output
# [[1], [2]]	[1,1]
# [[1, 2], [3, 4], [5]]	[2,2,1]
def solution(mylist):
    answer = list(map(len, mylist))
    return answer

###################################################################################################
### sequence 멤버를 하나로 이어붙이기

# my
def solution(mylist):
    answer = ''
    for i in mylist: answer += i
    return answer

# good
my_list = ['1', '100', '33']
answer = ''.join(my_list)


###################################################################################################
### 삼각형 별찍기


# my & good
n = int(input().strip())
a = 1
while True:
    if a > n: break
    print('*' * a)
    a += 1


###################################################################################################
### 곱집합(Cartesian product) 구하기 - product

# my
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for i in iterable1:
    for j in iterable2:
        for k in iterable3:
            print(i+j+k)

# good
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)


###################################################################################################
### 2차원 리스트를 1차원 리스트로 만들기 - from_iterable

# my
def solution(mylist):
    answer = []
    for i in mylist:
        for j in i:
            answer.append(j)
    return answer

# good
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()


###################################################################################################
### 순열과 조합

# my
def solution(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

# good
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기


###################################################################################################
### 가장 많이 등장하는 알파벳 찾기

# my
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0


###################################################################################################
### for 문과 if문을 한번에

# my
def solution(mylist):
    answer = []
    for i in mylist:
        if i & 1: continue
        else: answer.append(i * i)
    return answer

# good
mylist = [3, 2, 6, 7]
answer = [i**2 for i in mylist if i %2 == 0]


###################################################################################################
### flag OR for-else

# my
import math
numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')


###################################################################################################
### 두 변수의 값 바꾸기 - swap

# my
a = 3
b = 'abc'

a, b = b, a # 참 쉽죠?


###################################################################################################
### 이진 탐색하기 - binary search

# my
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))

# good
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))


###################################################################################################
### 클래스 인스턴스 출력하기 - class의 자동 string casting

# my
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y

point = Coord(1, 2)
print( '({}, {})'.format(point.x, point.y) )

# 또는
def print_coord(coord):
    print( '({}, {})'.format(coord.x, coord.y) )
print_coord(point)

# good
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)


###################################################################################################
### 가장 큰 수, inf 혹은 가장 작은 수

# my good
min_val = float('inf')
min_val > 10000000000
max_val = float('-inf')


###################################################################################################
### 파일 입출력 간단하게 하기

# my good
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
