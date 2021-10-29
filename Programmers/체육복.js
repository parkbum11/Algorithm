function solution(n, lost, reserve) {
  var answer = 0;
  let arr = new Array(n + 2).fill(1);
  arr[0] = 0;
  arr[-1] = 0;
  for (const i of lost) {
    arr[i] -= 1;
  }
  for (const i of reserve) {
    arr[i] += 1;
  }
  for (let i = 1; i < n + 1; i++) {
    if (arr[i] === 0) {
      if (arr[i - 1] > 1) {
        arr[i - 1] -= 1
        arr[i] += 1
        answer += 1
      } else if (arr[i + 1] > 1) {
        arr[i + 1] -= 1
        arr[i] += 1
        answer += 1
      }
    } else {
      answer += 1
    }
  }
  console.log(answer);
  return answer;
}

solution(5, [2, 4], [1, 3, 5])