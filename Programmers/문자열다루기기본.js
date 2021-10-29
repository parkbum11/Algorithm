function solution(s) {
  var answer = true;
  if (s.length === 4 || s.length === 6) {
      for (const i of s) {
          let as = i.charCodeAt(0)
          if (as < 48 || as > 57) {
              answer = false;
              break
          }
      }
  } else {
      answer = false;
  }
  return answer;
}