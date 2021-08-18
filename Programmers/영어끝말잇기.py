def solution(n, words):
    answer = [0, 0]
    dict, past_word = {}, words[0][0]
    for index, word in enumerate(words):
        if past_word[-1] != word[0] or word in dict:
            answer[0] = (index % n) + 1
            answer[1] = (index // n) + 1
            break
        else:
            dict[word] = True
            past_word = word
    print(answer)

    return answer
solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])