def solution(record):
    answer = []
    users = {}
    inout = []
    for i in record:
        order = i.split()
        if order[0] == 'Enter':
            users[order[1]] = order[2]
            inout.append((order[1], 'in'))
        elif order[0] == 'Leave':
            inout.append((order[1], 'out'))
        else:
            users[order[1]] = order[2]
    for who, what in inout:
        if what == 'in':
            answer.append(users[who] + '님이 들어왔습니다.')
        else:
            answer.append(users[who] + '님이 나갔습니다.')
    # print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])