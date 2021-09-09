def solution(dirs):
    answer = 0
    flag = [[''] * 11 for _ in range(11)]
    info = {'U': ['D', [-1, 0]], 'D': ['U', [1, 0]], 'R': ['L', [0, 1]], 'L': ['R', [0, -1]]} # U D R L
    location = [5, 5]
    for dir in dirs:
        if location[0] + info[dir][1][0] < 0 or location[1] + info[dir][1][1] < 0 or location[0] + info[dir][1][0] >= 11 or location[1] + info[dir][1][1] >= 11: continue
        if dir not in flag[location[0]][location[1]]:
            answer += 1
            flag[location[0]][location[1]] += dir
            flag[location[0] + info[dir][1][0]][location[1] + info[dir][1][1]] += info[dir][0]
        location[0] += info[dir][1][0]
        location[1] += info[dir][1][1]
    return answer

solution("RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU")

# 다른 사람 풀이 이게 더 빠름
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2