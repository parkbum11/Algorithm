# 정확성, 효율성 둘 다 절반 맞음

def solution(n, k, cmd):
    result = ['O'] * n
    c_list = []
    for i in cmd:
        if i[0] == 'U':
            cnt = int(i[2])
            while cnt:
                k -= 1
                if result[k] == 'X':
                    k -= 1
                cnt -= 1

        elif i[0] == 'D':
            cnt = int(i[2])
            while cnt:
                k += 1
                if result[k] == 'X':
                    k += 1
                cnt -= 1

        elif i[0] == 'C':
            c_list.append(k)
            result[k] = 'X'
            k += 1
            if k >= n:
                k -= 2

        elif i[0] == 'Z':
            check = c_list.pop()
            result[check] = 'O'

    answer = ''.join(result)
    print(answer)
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
