/**
 * 시간초과 풀이 O(N^2)
 * @param {*} n 
 * @param {*} left 
 * @param {*} right 
 * @returns 
 */
function solution(n, left, right) {
   const answer = [];
  
  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j ++) {
      if (i < j) {
        answer.push(j);
      }else {
        answer.push(i);
      }
    }
  }
    
  return answer.slice(left, right + 1);
}

/**
 * 통과 풀이 O(N)
 * @param {*} n 
 * @param {*} left 
 * @param {*} right 
 * @returns 
 */
function solution(n, left, right) {
   const answer = [];
  
   for (let i = left; i < right + 1; i++) {
    
    const value = Math.floor(i/n);
    const rest = i % n;
    
    if (value >= rest) {
      answer.push(value + 1);
    }else {
      answer.push(rest + 1);
    }
  }
  
  return answer;
}