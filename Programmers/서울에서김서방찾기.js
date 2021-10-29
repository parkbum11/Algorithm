function solution(seoul) {
  var answer = 0;
  for (const i in seoul) {
    if (seoul[i] === 'Kim') {
      answer = i;
      break
    }
  }
  return `김서방은 ${answer}에 있다`;
}

solution(["Jane", "Kim"])