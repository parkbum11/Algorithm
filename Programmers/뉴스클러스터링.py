import math

def makedict(st):
    info = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    dic = {}
    st = st.upper()
    for i in range(0, len(st)):
        check_st = st[i:i+2]
        if len(check_st) != 2: continue
        for j in check_st:
            if j not in info:
                break
        else:
            if check_st in dic:
                dic[check_st] += 1
            else:
                dic[check_st] = 1
    return dic
def solution(str1, str2):
    answer = 65536
    dic1 = makedict(str1)
    dic2 = makedict(str2)
    if len(dic1) == 0 and len(dic2) == 0: return answer
    minn, maxx = 0, 0
    for i, val in dic1.items():
        if i not in dic2:
            maxx += val
        else:
            minn += min(dic1[i], dic2[i])
            maxx += max(dic1[i], dic2[i])
    for i, val in dic2.items():
        if i not in dic1:
            maxx += val
    answer *= (minn / maxx)
    # print(minn, maxx)
    # print(math.floor(answer))
    return math.floor(answer)

solution('E=M*C^2', 'e=m*c^2')