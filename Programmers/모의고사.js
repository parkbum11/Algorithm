function solution(answers) {
    var answer = [];
    let one_ans = [1, 2, 3, 4, 5];
    let two_ans = [2, 1, 2, 3, 2, 4, 2, 5];
    let three_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    let one_loc = 0;
    let two_loc = 0;
    let three_loc = 0;
    let one_cnt = 0;
    let two_cnt = 0;
    let three_cnt = 0;
    let one_length = 5;
    let two_length = 8;
    let three_length = 10;

    for (const element of answers) {
        if (element === one_ans[one_loc]) {
            one_cnt += 1
        }
        if (element === two_ans[two_loc]) {
            two_cnt += 1
        }
        if (element === three_ans[three_loc]) {
            three_cnt += 1
        }
        one_loc = (one_loc + 1) % one_length
        two_loc = (two_loc + 1) % two_length
        three_loc = (three_loc + 1) % three_length
    }

    let maxx = Math.max(one_cnt, two_cnt, three_cnt)

    if (maxx === one_cnt) {
        answer.push(1)
    } 
    if (maxx === two_cnt) {
        answer.push(2)
    } 
    if (maxx === three_cnt) {
        answer.push(3)
    }

    return answer;
}