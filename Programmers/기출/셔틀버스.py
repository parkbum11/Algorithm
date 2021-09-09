def solution(n, t, m, timetable):
    answer = ''
    minTimeTable = []
    for i in timetable:
        time = int(i[:2]) * 60 + int(i[3:]) * 1
        minTimeTable.append(time)
    minTimeTable.sort()

    # 버스 운행
    nowtime = 540
    lasttime = nowtime + (n - 1) * t
    index = 0
    passenger = 0
    for time in range(nowtime, lasttime + 1, t):
        nowtime = time
        if index >= len(timetable): break
        passenger = 0
        if minTimeTable[index] <= time:
            while True:
                if index >= len(timetable) or passenger >= m: break
                if minTimeTable[index] > time: break
                passenger += 1
                index += 1
    if passenger < m or nowtime < lasttime:
        answer = lasttime
    else:
        answer = minTimeTable[index - 1] - 1

    hour = str(answer // 60)
    minit = str(answer % 60)
    if len(hour) == 1: hour = '0' + hour
    if len(minit) == 1: minit = '0' + minit
    answer = hour + ':' + minit
    return answer


solution(2, 10, 2, ["09:10", "09:09", "08:00"])