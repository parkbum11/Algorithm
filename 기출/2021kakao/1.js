function solution(gift_cards, wants) {
  let answer = 0;
  let cnt = 0
  let info = [];



  for (let i = 0; i < wants.length; i++) {
    info.push(0)
  }
  
  for (let i = 0; i < gift_cards.length; i++) {
    for (let j = 0; j < wants.length; j++) {
      if (gift_cards[i] === wants[j] && info[j] === 0) {
        info[j] = 1
        cnt += 1
        break
      }
    }
  }

  answer = wants.length - cnt
  // console.log(answer);
  return answer;
}

solution([5, 4, 5, 4, 5], [1, 2, 3, 5, 4])