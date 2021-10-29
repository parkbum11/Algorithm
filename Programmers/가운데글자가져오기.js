function solution(s) {
  var answer = '';
  let len = s.length
  let half = Math.floor(len / 2)
  if (len % 2 === 0) {
    answer += s[half - 1]
    answer += s[half]
  } else {
    answer += s[half]
  }
  console.log(answer);
  return answer;
}

solution('qwer')