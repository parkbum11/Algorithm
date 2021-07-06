let set = new Set();
numOfCase([1,7],'')
function numOfCase(arr,str) {
	if(arr.length) {
    	for(let i = 0; i <arr.length; i++) {
        	let copy = [...arr];
          	copy.splice(i,1);
          	numOfCase(copy,str + arr[i])
        }
    }
  	if(str > 0) set.add(Number(str))
}
console.log(Array.from(set)) 