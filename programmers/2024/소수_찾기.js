// 소수 찾기

// 에라토스테네스의 체

function solution(n) {
    const arr = Array(n + 1).fill(0).map((v, i) => i + 1);
    const answer = [];
    
    for (let i = 2; i <= n; i++) {
      if (arr[i] === 0) continue;
      
      for (let j = 2*i; j <= n; j += i) {
        arr[j] = 0;
      }
    }
    
    for (let i = 2; i <= n; i++) {
      if (arr[i] !== 0) answer.push(i);
    }
    
    return answer.length;
  }
  
  solution(10);