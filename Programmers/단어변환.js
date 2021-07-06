function solution(begin, target, words) {
    var answer = -1;
    
    for (const i of words) {
        if (i === target) {
            answer = 0
        }
    }
    
    if (answer === -1) {
        return 0
    }
    
    let q = [[begin, 0]];
    
    while (q) {
        let qq = q.shift();
        if (qq[0] === target) {
            answer += qq[1]
            break
        }
        for (const value of words) {
            let cnt = 0;
            for (let i = 0; i < value.length; i++) {
                if (qq[0][i] !== value[i]) {
                    cnt += 1
                }
                if (cnt > 1) {
                        break
                    }
            }
            if (cnt === 1) {
                q.push([value, qq[1] + 1])
            }
        }
    }
    
    return answer;
}