function solution(arr, divisor) {
  var answer = [];
  arr.sort((a, b) => a - b);
  arr.forEach(e => {
    if (e % divisor === 0) {
      answer.push(e);
    }
  });
  if (arr.length === 0) {
    answer.push(-1);
  }
  return answer;
}