def solution(files):
    answer = []
    new_files = []
    for file in files:
        plus = [file]
        file = file.lower()
        for index, i in enumerate(file):
            if 48 <= ord(i) <= 57:
                plus.append(file[:index])
                last_index = index + 1
                while len(file) > last_index and 48 <= ord(file[last_index]) <= 57:
                    last_index += 1
                    # if len(file) <= last_index: break
                plus.append(int(file[index:last_index]))
                break
        new_files.append(plus)
        print(plus)
    new_files.sort(key=lambda x: x[1:3])
    for file in new_files: answer.append(file[0])
    return answer

solution(["F15", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])