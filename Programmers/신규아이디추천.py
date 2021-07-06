def second(id):
    new_id = ''
    for i in id:
        num = ord(i)
        if 48 <= num <= 57 or 97 <= num <= 122 or num == 45 or num == 46 or num == 95: new_id += i
    return new_id

def solution(new_id):
    new_id = second(new_id.lower())
    new_id_id = ''
    cnt = 0
    for i in new_id:
        if i == '.':
            cnt += 1
            if cnt == 1:
                new_id_id += i
        else:
            cnt = 0
            new_id_id += i
    new_id = new_id_id
    if len(new_id) == 0: new_id = 'a'
    if new_id[0] == '.': new_id = new_id[1:]
    if len(new_id) == 0: new_id = 'a'
    if new_id[-1] == '.': new_id = new_id[:-1]
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    answer = new_id
    return answer

print(solution('abcdefghijklmn.p'))

######################################################
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st