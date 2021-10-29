function solution(s){
  var answer = true;
  let num_p = 0;
  let num_y = 0;
  for (const i of s) {
    if (i === 'p' || i === 'P') {
      num_p += 1
    } else if (i === 'y' || i === 'Y') {
      num_y += 1
    }
  }
  console.log(num_p, num_y);
  return num_p == num_y ? true : false;
}
