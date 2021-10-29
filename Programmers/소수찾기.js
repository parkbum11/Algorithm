// let set = new Set();
// numOfCase([1,7],'')
// function numOfCase(arr,str) {
// 	if(arr.length) {
//     	for(let i = 0; i <arr.length; i++) {
//         	let copy = [...arr];
//           	copy.splice(i,1);
//           	numOfCase(copy,str + arr[i])
//         }
//     }
//   	if(str > 0) set.add(Number(str))
// }
// console.log(Array.from(set)) 

function solution(n) {
  var answer = n - 1;
  let info = new Array(n + 1).fill(0)
  for (let i = 2; i ** 2 < n; i++) {
    console.log(i);
    let j = 3;
    let num = i * 2;
    while (num <= n) {
      if (info[num] === 0) {
        answer -= 1;
        info[num] = 1;
      }
      num = i * j;
      j += 1
    }
    console.log(info);
  }
  console.log(answer);
  return answer;
}
solution(10)