def solution(fees, records):
    answer = []
    car_records = {}
    car_fee = {}
    for i in records:
        infos = i.split()
        time = int(infos[0][:2]) * 60 + int(infos[0][3:])
        if infos[1] in car_records:
            car_records[infos[1]].append(time)
        else:
            car_records[infos[1]] = [time]

    answer = sorted(car_records.keys())

    for key, value in car_records.items():
        time = 0
        fee = 0
        # calcu time
        if len(value) & 1:
            value.append(24 * 60 - 1)
        for i in range(0, len(value), 2):
            time += value[i + 1] - value[i]
        # calcu fee for each
        time -= fees[0]
        if time > 0:
            q, r = divmod(time, fees[2])
            if r != 0:
                fee += fees[3] * (q + 1)
            else:
                fee += fees[3] * q
        fee += fees[1]
        car_fee[key] = fee

    for i in range(len(answer)):
        answer[i] = car_fee[answer[i]]
    print(answer)


    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])