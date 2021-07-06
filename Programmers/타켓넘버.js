var answer = 0;
function solution(numbers, target) {
    const leng = numbers.length;
    DFS(numbers, 0, 0, leng, target)
    return answer;
}

function DFS(numbers, number, index, length, tar) {
    
    if (index === length) {
        
        if (number === tar) {
            answer += 1
        }
        return
    }
    DFS(numbers, number + numbers[index], index + 1, length, tar)
    DFS(numbers, number - numbers[index], index + 1, length, tar)
}