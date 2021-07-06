function solution(brown, yellow) {
    var answer = [];
    let summ = brown + yellow;

    for (let i = 3; i <= summ; i++) {
        if (summ % i === 0) {
            let check = summ - (i + parseInt(summ / i)) * 2 + 4;
            if (check === yellow) {
                answer.push(Math.max(i, parseInt(summ / i)))
                answer.push(Math.min(i, parseInt(summ / i)))
                break
            }
        }
    }

    return answer;
}