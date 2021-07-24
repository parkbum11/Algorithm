def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin1 = bin(arr1[i])[2:]
        bin2 = bin(arr2[i])[2:]
        line = ''
        while len(bin1) < n:
            bin1 = '0' + bin1
        while len(bin2) < n:
            bin2 = '0' + bin2
        for j in range(n):
            if bin1[j] == '1' or bin2[j] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer

solution(6, [46, 33, 33, 22, 31, 50], [27 ,56, 19, 14, 14, 10])