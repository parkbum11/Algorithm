function solution(price, money, count) {
  var answer = money;
  for (let i = 1; i < count + 1; i++) {
    answer -= price * i
  }
  console.log(answer);
  return answer < 0 ? answer * (-1) : 0;
}

solution(3, 20, 4)