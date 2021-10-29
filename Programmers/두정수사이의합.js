function solution(a, b) {
  var answer = 0;
  let big = Math.max(a, b);
  let small = Math.min(a, b);
  for (let i = small; i < big + 1; i++) {
    answer += 1
  }
  return answer;
}