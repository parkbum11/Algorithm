from collections import deque

dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


def BFS(i, j, place):
    q = deque()
    q.append((i, j, 0))
    flag = [(i, j)]
    print(place)
    while q:
        r, c, cnt = q.popleft()

        if cnt == 2:
            continue

        for k in range(4):
            rr, cc = r + dr[k], c + dc[k]
            print(rr, cc)
            if rr < 0 or rr >= 5 or cc < 0 or cc >= 5 or (rr, cc) in flag:
                continue

            if place[rr][cc] == 'X':
                continue
            elif place[rr][cc] == 'O':
                q.append((rr, cc, cnt + 1))
                flag.append((rr, cc))
            elif place[rr][cc] == 'P':
                print('dfdf')
                return 0
    return 1


def case(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if BFS(i, j, place) == 0:
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(case(place))

    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])