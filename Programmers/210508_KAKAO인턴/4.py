# ㅅㅂ 거의 다 틀림 6/30

result = 0

def DFS(room, time, roads, traps, end, maxx):
    global result
    if room == end:
        result = time
        return

    if time >= maxx:
        return

    if room in traps:
        a = traps.index(room)
        for i in range(len(roads)):
            if roads[i][0] == room or roads[i][1] == room:
                roads[i][0], roads[i][1] = roads[i][1], roads[i][0]
    for i in roads:
        if i[0] == room:
            DFS(i[1], time + i[2], roads, traps, end, maxx)

    if room in traps:
        a = traps.index(room)
        for i in range(len(roads)):
            if roads[i][0] == room or roads[i][1] == room:
                roads[i][0], roads[i][1] = roads[i][1], roads[i][0]


def solution(n, start, end, roads, traps):
    answer = 987654321
    maxx = 0
    start_list = []
    for i in roads:
        maxx += i[2]
        if i[0] == start:
            start_list.append((i[1], i[2]))
    maxx *= 2
    for i, j in start_list:
        DFS(i, j, roads, traps, end, maxx)
        if result < answer:
            answer = result
    return answer


solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])