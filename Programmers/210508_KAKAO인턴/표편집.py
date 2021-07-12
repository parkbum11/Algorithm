# 정확성, 효율성 둘 다 절반 맞음

def solution(n, k, cmd):
    info = ['O'] * n
    c_li = []

    for i in cmd:
        if i[0] == 'D':
            for _ in range(int(i[2])):
                k += 1
                while True:
                    if info[k] == 'O':
                        break
                    k += 1
        elif i[0] == 'U':
            for _ in range(int(i[2])):
                k -= 1
                while True:
                    if info[k] == 'O':
                        break
                    k -= 1
        elif i[0] == 'C':
            info[k] = 'X'
            c_li.append(k)
            for j in range(k, n):
                if info[j] == 'O':
                    k = j
                    break
            else:
                k -= 1
        elif i[0] == 'Z':
            index = c_li.pop()
            info[index] = 'O'

    answer = ''.join(info)
    print(answer)
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
