function solution(arr)
{
    var answer = [];
    let num = -1;
    for (const i of arr) {
      if (num !== i) {
        num = i;
        answer.push(i)
      }
    }
    return answer;
}