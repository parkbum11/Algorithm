import math
def primeNumberOrNot(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def TentoN(num, n):
    result = ''
    q, r = divmod(num, n)
    while q > 0:
        result = str(r) + result
        q, r = divmod(q, n)
    result = str(r) + result
    return result

def solution(n, k):
    answer = 0
    # change num 10 to k
    if k == 10:
        new_num = str(n)
    else:
        new_num = TentoN(n, k)

    split_new_num = new_num.split('0')

    for i in split_new_num:
        if len(i) == 0 or i == '1': continue
        test = primeNumberOrNot(int(i))
        if test == True:
            answer += 1
    return answer


solution(1101011, 10)