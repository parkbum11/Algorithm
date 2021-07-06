function solution(n, passenger, train) {
  var answer = [0, 0];

  let info = [];
  let flag = [];
  let q = [];

  for (let i = 0; i < n + 1; i++) {
    info.push([])
    flag.push(0)
  }

  for (let i = 0; i < train.length; i++) {
    info[train[i][0]].push(train[i][1])
    info[train[i][1]].push(train[i][0])
  }
  
  passenger.unshift(0)
  flag[1] = 1
  for (let i = 0; i < info[1].length; i++) {
    q.push([info[1][i], passenger[info[1][i]] + passenger[1]])
    // flag[info[1][i]] = 1
  }
  console.log(info);
  
  while (q.length > 0) {
    let qq = q.shift()
    let cnt = 0

    console.log(q);

    flag[qq[0]] = 1
    for (let i = 0; i < info[qq[0]].length; i++) {
      if (flag[info[qq[0]][i]] === 0) {
        let new_p = passenger[info[qq[0]][i]];
        q.push([info[qq[0]][i], qq[1] + new_p])
        cnt += 1
      }
    }
    if (cnt === 0) {
      if (qq[1] > answer[1]) {
        answer[0] = qq[0]
        answer[1] = qq[1]
      }
      else if (qq[1] === answer[1] && qq[0] > answer[0]) {
        answer[0] = qq[0]
        answer[1] = qq[1]
      }
    }
  }
  console.log(answer);

  return answer;
}

solution(6, [1,1,1,1,1,1], [[1,2],[1,3],[1,4],[3,5],[3,6]])