def solution(phone_number):
    answer = -1
    cnt = phone_number.count('+')
    phone_number = phone_number.split('-')
    if len(phone_number) == 3 and cnt == 0:
        if phone_number[0] == '010' and len(phone_number[1]) == 4 and len(phone_number[2]) == 4:
            answer = 1
    elif len(phone_number) == 1 and cnt == 0:
        if phone_number[0][:3] == '010' and len(phone_number[0]) == 11:
            answer = 2
    elif len(phone_number) == 4 and cnt == 1:
        if phone_number[0] == '+82' and phone_number[1] == '10' and len(phone_number[2]) == 4 and len(phone_number[3]) == 4:
            answer = 3
    return answer


solution('+82-10-3434-2323')
solution('0102131231331')