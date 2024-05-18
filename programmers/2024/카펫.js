function solution(brown, yellow) {
    const totalCnt = brown + yellow;
    
    const results = [];
    
    // 약수 찾기
    
    for (let i = totalCnt; i >= 1; i --) {
      if (totalCnt % i === 0) {
        results.push(i);
      } 
    }
    
    if (results.length % 2 === 0) {
      
      for (let i = 0; i < results.length / 2; i ++) {
        const [가로, 세로] = [(results.length / 2) - i - 1, results.length / 2 + i]
        
        if ((results[가로] * 2) + (results[세로] * 2) - 4 === brown) {
          return [results[가로], results[세로]]
        }
      }
    }else {
      return [results[Math.floor(results.length / 2)], results[Math.floor(results.length / 2)]]
    }
  }
  
  solution(18, 6);
  
  