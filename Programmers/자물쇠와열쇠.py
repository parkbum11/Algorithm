def solution(key, lock):
    length = len(lock) + (len(key) - 1) * 2
    arr = [[0] * length for _ in range(length)]

    # 가운데 배치
    for i in range(len(lock)):
        for j in range(len(lock)):
            arr[i + (len(key) - 1)][j + (len(key) - 1)] = lock[i][j]

    # 미리 돌려 놓기
    new_key = [[[] * len(key) for _ in range(len(key))] for _ in range(len(key))]
    for _ in range(4):
        key = list(zip(*key[::-1]))
        for i in range(len(key)):
            for j in range(len(key)):
                new_key[i][j].append(key[i][j])

    # 열쇠 끼고 빼기 및 확인
    for i in range((len(key) - 1) + len(lock)):
        for j in range((len(key) - 1) + len(lock)):
            for k in range(4):
                # 끼기
                for ii in range(len(key)):
                    for jj in range(len(key)):
                        arr[i + ii][j + jj] += new_key[ii][jj][k]
                # 확인
                check = True
                for r in range((len(key) - 1), (len(key) - 1) + len(lock)):
                    for c in range((len(key) - 1), (len(key) - 1) + len(lock)):
                        if arr[r][c] != 1:
                            check = False
                            break
                    if check == False: break
                if check == True:
                    return True
                # 빼기
                for ii in range(len(key)):
                    for jj in range(len(key)):
                        arr[i + ii][j + jj] -= new_key[ii][jj][k]
    return False


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])