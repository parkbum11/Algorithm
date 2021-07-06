function solution(needs, r) {
  let answer = 0;
  let info = {};

  if (r === 0) {
    return answer
  }

  for (let i = 0; i < needs.length; i++) {
    let aa = '';
    for (let j = 0; j < needs[i].length; j++) {
      if (needs[i][j] == 1) {
        let a = String(j)
        aa += a
      }
      if (aa.length > r) {
        break
      }
    }
    if (aa.length <= r) {
      if (aa in info) {
        info[aa] += 1
      }
      else {
        info[aa] = 1
      }
    }
  }

  for (let key1 in info) {
    let cnt = 0;
    for (let key2 in info) {
      if (key1.includes(key2)) {
        cnt += info[key2]
      }
    }

    if (cnt > answer) {
      answer = cnt
    }
  }
  console.log(answer);
  return answer;
}

solution([ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ], 2)