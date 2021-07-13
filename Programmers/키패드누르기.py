def solution(numbers, hand):
    answer = ''
    left_h = 10
    right_h = 12
    info = [0, (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]

    for i in numbers:
        if i == 0: i += 11
        if i == 1 or i == 4 or i == 7: answer += 'L'; left_h = i
        elif i == 3 or i == 6 or i == 9: answer += 'R'; right_h = i
        else:
            dist_l = abs(info[i][0] - info[left_h][0]) + abs(info[i][1] - info[left_h][1])
            dist_r = abs(info[i][0] - info[right_h][0]) + abs(info[i][1] - info[right_h][1])

            if dist_r > dist_l: answer += 'L'; left_h = i
            elif dist_r < dist_l: answer += 'R'; right_h = i
            else:
                if hand == 'left': answer += 'L'; left_h = i
                else: answer += 'R'; right_h = i
    # print(answer)
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
# "LRLLLRLLRRL"