# C, C#, D, D#, E, F, F#, G, G#, A, A#, B 총 12개
# C# -> 3, D# -> 4, F# -> 6, G# -> 7, A# -> 1
def changeMusic(old):
    new = old
    change_info = {'C#': '3', 'D#': '4', 'F#': '6', 'G#': '7', 'A#': '1'}
    for info in change_info: new = new.replace(info, change_info[info])
    return new

def solution(m, musicinfos):
    answer = ['', 0]
    m = changeMusic(m)
    for i in musicinfos:
        musicinfo = i.split(',')
        musicinfo[3] = changeMusic(musicinfo[3])
        # if musicinfo[1] == '00:00': musicinfo[1] = '24:00'
        time = ((int(musicinfo[1][:2]) - int(musicinfo[0][:2])) * 60) + (int(musicinfo[1][3:]) - int(musicinfo[0][3:]))
        cal_time = (time // len(musicinfo[3])) + 1
        musicinfo[3] = musicinfo[3] * cal_time
        musicinfo[3] = musicinfo[3][:time]
        # print(musicinfo)
        if m in musicinfo[3]:
            if answer[1] < time:
                answer = [musicinfo[2], time]
    # print(answer[0])
    return answer[0]

solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])