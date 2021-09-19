def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_num = {}
    report_info = {}
    report_li = []
    for i in id_list:
        report_num[i] = 0
        report_info[i] = set()
    for i in report:
        i = i.split()
        report_info[i[0]].add(i[1])
    for i in report_info.values():
        for v in i:
            report_num[v] += 1
    for key, value in report_num.items():
        if value >= k:
            report_li.append(key)
    index = 0
    for value in report_info.values():
        for v in value:
            if v in report_li:
                answer[index] += 1
        index += 1

    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)