import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
while True:
    result = 'No'
    N = int(input())
    if N == 0:break
    room_info = [0]
    for i in range(1, N + 1):
        li = input().split()
        for j in range(1, len(li) - 1):
            li[j] = int(li[j])
        room_info.append(li[:-1])

    q = deque()
    q.append((1, 0))

    while q:
        room, money = q.popleft()
        new_money = 0

        if room_info[room][0] == 'E':
            new_money = money
        elif room_info[room][0] == 'L':
            if money >= room_info[room][1]:
                new_money = money
            else:
                new_money = room_info[room][1]
        elif room_info[room][0] == 'T':
            new_money = money - room_info[room][1]

        if new_money >= 0:
            if room == N:
                result = 'Yes'
                break
            else:
                for i in room_info[room][2:]:
                    q.append((i, new_money))
    print(result)